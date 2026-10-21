# Terraform and GitHub Actions Interview Prep

Integrated from the supplied study notes. Examples are focused snippets; placeholder IDs, provider versions and action SHAs must be selected for your environment. Commands shown are study examples, not executed deployments.

This guide summarizes the Terraform and GitHub Actions topics covered during prep. It is written for interview revision: concepts, examples, common traps, and interview-ready answers.

---

## Terraform

### 1. Terraform Variable Types

Terraform variables define input values for a module.

Common types:

```hcl
string
number
bool
list(string)
set(string)
map(string)
object({
  name = string
})
list(object({
  name  = string
  value = string
}))
map(object({
  instance_type = string
  disk_size     = number
}))
```

Example:

```hcl
variable "instances" {
  type = map(object({
    instance_type = string
    disk_size     = number
    public        = bool
  }))

  default = {
    app = {
      instance_type = "t3.micro"
      disk_size     = 20
      public        = true
    }
  }
}
```

Interview answer:

> Terraform types define the shape of input values. Primitive types include string, number, and bool. Collection and structural types like list, set, map, object, list(object), and map(object) are used for more complex reusable modules.

---

### 2. `for_each`

`for_each` creates one resource instance per item in a map or set.

```hcl
resource "aws_instance" "this" {
  for_each = var.instances

  ami           = "ami-1234567890abcdef0"
  instance_type = each.value.instance_type

  tags = {
    Name = each.key
  }
}
```

If:

```hcl
instances = {
  app = {
    instance_type = "t3.micro"
  }

  worker = {
    instance_type = "t3.small"
  }
}
```

Terraform creates:

```text
aws_instance.this["app"]
aws_instance.this["worker"]
```

Key idea:

```text
each.key   = map key
each.value = map value/object
```

Use `for_each` when each instance has a meaningful stable key.

---

### 3. `count`

`count` creates N copies of a resource.

```hcl
resource "aws_instance" "web" {
  count = 2

  ami           = "ami-1234567890abcdef0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}
```

Terraform creates:

```text
aws_instance.web[0]
aws_instance.web[1]
```

`count.index` starts at `0`.

Use `count` for simple identical resources or 0/1 conditional resources:

```hcl
count = var.create_instance ? 1 : 0
```

Prefer `for_each` for named resources because `count` indexes can shift if list order changes.

---

### 4. `locals`

`locals` define reusable calculated values inside a module.

```hcl
locals {
  environment = "dev"
  app_name    = "billing"
  name_prefix = "${local.environment}-${local.app_name}"
}
```

Use with:

```hcl
local.name_prefix
```

Difference:

```text
variable = input from outside
local    = calculated/reusable value inside Terraform
output   = value exposed after apply
```

Common uses:

```hcl
locals {
  common_tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
```

---

### 5. `merge`

`merge` combines maps/objects.

```hcl
locals {
  common_tags = {
    Environment = "dev"
    Project     = "billing"
  }
}

tags = merge(local.common_tags, {
  Name = "dev-billing-app"
})
```

Result:

```hcl
{
  Environment = "dev"
  Project     = "billing"
  Name        = "dev-billing-app"
}
```

If duplicate keys exist, the later map wins:

```hcl
merge({ Environment = "dev" }, { Environment = "prod" })
```

Result:

```hcl
{ Environment = "prod" }
```

---

### 6. `concat`

`concat` joins lists.

```hcl
locals {
  public_subnets  = ["subnet-111", "subnet-222"]
  private_subnets = ["subnet-333"]

  all_subnets = concat(local.public_subnets, local.private_subnets)
}
```

Result:

```hcl
["subnet-111", "subnet-222", "subnet-333"]
```

Comparison:

```text
merge  = combine maps
concat = combine lists
```

`concat` does not remove duplicates. Use `distinct(concat(...))` if uniqueness is needed.

---

### 7. `set`, `list`, and Ordering

`list`:

```text
ordered
duplicates allowed
index access works
```

Example:

```hcl
["dev", "qa", "prod"]
```

Indexes:

```text
0 = dev
1 = qa
2 = prod
```

`set`:

```text
unordered
duplicates removed
no stable index
```

Example:

```hcl
toset(["dev", "qa", "dev"])
```

Result:

```hcl
["dev", "qa"]
```

Mental model:

```text
list = ordered queue
set  = unique basket
map  = named values
```

---

### 8. `tomap`

`tomap` converts a value into a map.

```hcl
locals {
  instances = tomap({
    app = {
      instance_type = "t3.micro"
    }
  })
}
```

Useful when Terraform needs help with type inference, especially conditionals:

```hcl
instances = var.create_instances ? tomap({
  app = {
    instance_type = "t3.micro"
  }
}) : tomap({})
```

---

### 9. Dynamic Blocks

`dynamic` generates repeated nested blocks inside a resource.

Resource-level `for_each` creates multiple resources.

`dynamic` creates multiple nested blocks inside one resource.

Example:

```hcl
variable "security_rules" {
  type = list(object({
    name     = string
    priority = number
    port     = string
  }))
}

resource "azurerm_network_security_group" "this" {
  name                = "demo-nsg"
  location            = "westus2"
  resource_group_name = azurerm_resource_group.rg.name

  dynamic "security_rule" {
    for_each = var.security_rules

    content {
      name                       = security_rule.value.name
      priority                   = security_rule.value.priority
      direction                  = "Inbound"
      access                     = "Allow"
      protocol                   = "Tcp"
      source_port_range          = "*"
      destination_port_range     = security_rule.value.port
      source_address_prefix      = "*"
      destination_address_prefix = "*"
    }
  }
}
```

Interview answer:

> A dynamic block generates repeated nested blocks from a collection. It is used when the provider schema expects repeatable blocks like security_rule, ingress, egress, network_acls, statement, condition, or origin.

---

### 10. Modules

A module is a reusable group of Terraform files.

Example:

```hcl
module "app_server" {
  source = "./modules/ec2"

  ami           = "ami-1234567890abcdef0"
  instance_type = "t3.micro"
  name          = "app-server"
}
```

Flow:

```text
root module calls child module
inputs go into module variables
module creates resources
module outputs can be read by root
```

Every Terraform folder is a module. The folder where Terraform runs is the root module.

---

### 11. Module Outputs and Dependencies

Child module output:

```hcl
output "subnet_id" {
  value = azurerm_subnet.app.id
}
```

Root module consuming output:

```hcl
module "app_service" {
  source = "./modules/app-service"

  subnet_id = module.network.subnet_id
}
```

This reference creates an implicit dependency:

```text
module.app_service depends on module.network
```

Prefer implicit dependencies through references.

Use `depends_on` only for hidden dependencies Terraform cannot infer.

---

### 12. `depends_on`

Terraform normally builds dependencies from references.

Example:

```hcl
resource_group_name = azurerm_resource_group.rg.name
```

This already creates a dependency on:

```hcl
azurerm_resource_group.rg
```

Example from prep:

```hcl
module "azure-key-vault" {
  resource_group_name = azurerm_resource_group.rg.name

  azurerm_role_assignments = {
    (azurerm_user_assigned_identity.this.principal_id) = {
      role_definition_name = "Key Vault Secrets Officer"
    }
  }
}
```

The module already depends on the resource group and user-assigned identity because it references them. Extra `depends_on` is usually redundant.

Interview answer:

> Terraform builds its dependency graph from references. I use explicit depends_on only when there is a hidden dependency that Terraform cannot infer.

---

### 13. Provider Configuration and `provider.tf`

A typical Azure `provider.tf` contains:

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.62.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstatedevsa"
    container_name       = "tfstate"
    key                  = "dev.tfstate"
  }
}

provider "azurerm" {
  features {}
  subscription_id = "11111111-1111-1111-1111-111111111111"
}
```

Meaning:

```text
required_providers = which providers/plugins Terraform needs
backend            = where Terraform state is stored
provider           = how Terraform talks to Azure and where resources are created
```

Important:

```text
backend "azurerm" controls state storage
provider "azurerm" controls resource creation
```

They can use the same Azure subscription, but they are separate concepts.

---

### 14. `features {}`

AzureRM provider requires:

```hcl
provider "azurerm" {
  features {}
}
```

It means:

```text
Use AzureRM provider with default feature settings.
```

You can customize provider behavior:

```hcl
provider "azurerm" {
  features {
    key_vault {
      purge_soft_deleted_secrets_on_destroy = true
    }

    resource_group {
      prevent_deletion_if_contains_resources = true
    }
  }
}
```

It does not create Azure resources. It configures provider behavior.

---

### 15. Provider Aliases

Provider aliases allow multiple configurations of the same provider.

Example: two Azure subscriptions.

```hcl
provider "azurerm" {
  features {}
  subscription_id = "dev-subscription-id"
}

provider "azurerm" {
  alias = "shared"

  features {}
  subscription_id = "shared-subscription-id"
}
```

Default provider:

```hcl
resource "azurerm_resource_group" "app" {
  name     = "app-rg"
  location = "westus2"
}
```

Aliased provider:

```hcl
resource "azurerm_resource_group" "shared" {
  provider = azurerm.shared

  name     = "shared-rg"
  location = "westus2"
}
```

Passing alias into a module:

```hcl
module "shared_key_vault" {
  source = "./modules/key-vault"

  providers = {
    azurerm = azurerm.shared
  }
}
```

Interview answer:

> Provider aliases let me manage resources across multiple subscriptions, accounts, or regions in the same configuration. Resources use the default provider unless `provider = azurerm.shared` is specified. Aliased providers must be passed explicitly to modules.

---

### 16. Terraform State and Resource Addresses

State maps Terraform addresses to real infrastructure.

Example:

```text
azurerm_resource_group.rg
  -> /subscriptions/.../resourceGroups/demo-rg
```

Resource addresses:

```text
azurerm_resource_group.rg
azurerm_resource_group.rg[0]
azurerm_resource_group.rg["dev"]
module.network.azurerm_subnet.app
```

Important:

```text
Terraform identity is based on the resource address, not only the cloud resource name.
```

If you rename:

```hcl
resource "azurerm_resource_group" "rg" {}
```

to:

```hcl
resource "azurerm_resource_group" "main" {}
```

Terraform sees old address removed and new address added unless you use a moved block.

Useful commands:

```bash
terraform state list
terraform state show <address>
terraform state mv <from> <to>
terraform state rm <address>
terraform import <address> <id>
terraform state pull
terraform force-unlock <lock-id>
```

---

### 17. Import

Use import when a real resource exists but Terraform does not manage it yet.

CLI:

```bash
terraform import azurerm_resource_group.rg /subscriptions/<sub-id>/resourceGroups/existing-rg
```

Config-driven import:

```hcl
resource "azurerm_resource_group" "rg" {
  name     = "existing-rg"
  location = "westus2"
}

import {
  to = azurerm_resource_group.rg
  id = "/subscriptions/<sub-id>/resourceGroups/existing-rg"
}
```

Meaning:

```text
Attach this existing Azure resource to this Terraform address.
```

---

### 18. Moved Blocks

Use `moved` when Terraform already manages a resource but its address changed.

Example:

```hcl
moved {
  from = azurerm_resource_group.old
  to   = azurerm_resource_group.new
}
```

Moving into a module:

```hcl
moved {
  from = azurerm_resource_group.rg
  to   = module.resource_group.azurerm_resource_group.this
}
```

Difference:

```text
import = real resource exists, state does not know it yet
moved  = state knows it, but Terraform address changed
```

---

### 19. `terraform init` Commands

Common init commands:

```bash
terraform init
terraform init -upgrade
terraform init -migrate-state
terraform init -reconfigure
terraform init -backend-config=dev.backend.hcl
terraform init -input=false
terraform init -backend=false
```

Meanings:

```text
init                  = initialize working directory
init -upgrade         = upgrade allowed provider/module versions
init -migrate-state   = move existing state to changed backend
init -reconfigure     = accept new backend config without migration
init -backend-config  = pass backend config externally
init -input=false     = disable prompts for CI/CD
init -backend=false   = skip backend initialization
```

---

### 20. `.terraform.lock.hcl`

`.terraform.lock.hcl` is Terraform's provider dependency lock file.

It records:

```text
exact provider versions
version constraints
provider checksums
```

Example:

```hcl
provider "registry.terraform.io/hashicorp/azurerm" {
  version     = "4.62.0"
  constraints = "~> 4.62.0"
  hashes = [
    "h1:..."
  ]
}
```

Why it matters:

```text
reproducible provider versions
consistent local and CI behavior
prevents surprise upgrades
verifies downloaded provider integrity
```

Usually commit it to Git.

Upgrade intentionally with:

```bash
terraform init -upgrade
```

---

### 21. Lifecycle Blocks

prevent_destroy is a planning guard while the lifecycle rule remains in configuration; deleting the whole resource block also removes that guard. Keep cloud-side deletion protections for critical data.

`lifecycle` changes how Terraform handles create, update, replace, and destroy.

Common options:

```hcl
lifecycle {
  prevent_destroy = true
}
```

Protects critical resources.

```hcl
lifecycle {
  ignore_changes = [
    tags["CostCenter"]
  ]
}
```

Ignores expected external changes.

```hcl
lifecycle {
  create_before_destroy = true
}
```

Tries to create replacement before destroying old resource.

```hcl
lifecycle {
  replace_triggered_by = [
    azurerm_service_plan.this.id
  ]
}
```

Forces replacement when another object changes.

Interview warning:

> Do not overuse `ignore_changes`; it can hide drift.

---

### 22. Plan and Apply Behavior

`terraform plan` previews changes.

```bash
terraform plan -input=false -no-color -out=infra.tfplan
```

`terraform apply` executes changes.

```bash
terraform apply -input=false infra.tfplan
```

Saved plan pattern:

```text
plan creates exact artifact
review/approval happens
apply uses that exact artifact
```

This avoids applying a different plan from the one reviewed.

Useful flag:

```bash
terraform plan -detailed-exitcode
```

Exit codes:

```text
0 = no changes
1 = error
2 = changes present
```

---

### 23. State Locking and CI/CD Concurrency

Remote backends lock state to prevent concurrent writes.

If two pipelines use the same backend key:

```text
run A gets lock
run B fails or waits
```

GitHub Actions fix:

```yaml
concurrency:
  group: terraform-dev-state
  cancel-in-progress: false
```

Terraform backup:

```bash
terraform plan -lock-timeout=20m
terraform apply -lock-timeout=20m
```

Avoid:

```bash
-lock=false
```

unless you really understand the risk.

---

### 24. Separating State Per Environment/Component

Avoid one giant state file.

Good:

```text
dvve/dev.tfstate
dvve/uat.tfstate
dvve/prod.tfstate
```

For larger systems:

```text
dvve/dev/network.tfstate
dvve/dev/app.tfstate
dvve/dev/database.tfstate
```

Benefits:

```text
smaller blast radius
less lock contention
faster plans
clearer ownership
better access control
```

Split state by what changes together and what should fail together.

---

### 25. `terraform_remote_state`

Reads outputs from another Terraform state file.

Network stack:

```hcl
output "app_subnet_id" {
  value = azurerm_subnet.app.id
}
```

App stack:

```hcl
data "terraform_remote_state" "network" {
  backend = "azurerm"

  config = {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "companytfstate"
    container_name       = "tfstate"
    key                  = "dvve/dev/network.tfstate"
  }
}
```

Use:

```hcl
subnet_id = data.terraform_remote_state.network.outputs.app_subnet_id
```

Important:

```text
remote_state exposes root outputs; its credentials may allow access to the entire state snapshot
state access should be protected
state may contain sensitive values
```

---

### 26. State Troubleshooting

Checklist:

```text
1. terraform state list
2. terraform state show <address>
3. Compare config, state, and Azure reality
4. Check provider subscription/alias
5. Check whether resource address changed
6. Use import if resource exists but is missing from state
7. Use moved/state mv if address changed
8. Use state rm only to stop managing without deleting
9. Avoid manual state edits
```

Interview answer:

> I troubleshoot state by checking whether the resource exists in state, whether the Terraform address is correct, whether the provider points to the expected subscription, and whether the real Azure resource still exists. Depending on the cause, I use import, moved blocks, state mv, or state rm.

---

### 27. Drift Detection

Drift means real infrastructure differs from Terraform config/state.

Detect:

```bash
terraform plan
```

CI-friendly:

```bash
terraform plan -detailed-exitcode -input=false -no-color
```

Refresh-only:

```bash
terraform plan -refresh-only
terraform apply -refresh-only
```

Normal plan:

```text
make infrastructure match config
```

Refresh-only:

```text
make state match real infrastructure
```

Interview answer:

> Drift detection identifies changes made outside Terraform. I use `terraform plan` to detect drift and decide whether to revert it, update code, use ignore_changes for expected external changes, or accept reality with refresh-only state updates.

---

### 28. Replace Behavior

Terraform replaces resources when a change cannot be updated in place.

Plan clues:

```text
-/ resource will be replaced
# forces replacement
```

Force replacement:

```bash
terraform apply -replace="azurerm_linux_virtual_machine.vm"
```

Modern preference:

```text
use -replace instead of old taint workflow
```

Be careful with critical resources:

```text
databases
storage accounts
key vaults
resource groups
networking
```

Use:

```hcl
lifecycle {
  prevent_destroy = true
}
```

for protection.

---

### 29. Targeting

`-target` limits Terraform to a specific resource/module.

```bash
terraform apply -target=module.network
```

Risk:

```text
partial apply
skipped changes
incomplete dependency reconciliation
confusing future plans
```

Use only for exceptional recovery/migration scenarios.

After targeted apply, always run:

```bash
terraform plan
```

without `-target`.

Interview answer:

> `-target` is a recovery tool, not a normal deployment strategy. It can leave infrastructure partially reconciled, so I use it only for exceptional cases and then run a full plan afterward.

---

### 30. Sensitive Data in State

Terraform state may contain secrets.

Example:

```hcl
resource "azurerm_key_vault_secret" "api_key" {
  name         = "api-key"
  value        = var.api_key
  key_vault_id = azurerm_key_vault.this.id
}
```

Even if:

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}
```

the secret value may still be in state.

Important:

```text
sensitive = true hides display
it does not guarantee absence from state
```

Best practice:

```text
Terraform creates Key Vault and permissions
separate secret pipeline writes actual secret values
apps use managed identity and Key Vault references
```

Never hardcode secrets in `variables.tf` defaults.

---

### 31. Variable Validation and Preconditions/Postconditions

Variable validation:

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "uat", "prod"], var.environment)
    error_message = "Environment must be dev, uat, or prod."
  }
}
```

Precondition:

```hcl
resource "azurerm_key_vault" "this" {
  # ...

  lifecycle {
    precondition {
      condition     = var.environment != "prod" || var.purge_protection_enabled
      error_message = "Production Key Vaults must have purge protection enabled."
    }
  }
}
```

Postcondition:

```hcl
lifecycle {
  postcondition {
    condition     = self.primary_location == azurerm_resource_group.rg.location
    error_message = "Storage account primary location must match RG location."
  }
}
```

Mental model:

```text
validation    = input guard
precondition  = before action guard
postcondition = after result guard
```

---

### 32. Provisioners

Provisioners run scripts or copy files during create/destroy.

Common types:

```text
local-exec
remote-exec
file
```

Example:

```hcl
provisioner "local-exec" {
  command = "echo Resource ${self.name} created"
}
```

Provisioners are a last resort because:

```text
not always idempotent
side effects are not fully tracked
can fail halfway
depend on runtime connectivity
blur infra and configuration management
```

Prefer:

```text
cloud-init/custom_data
Azure VM extensions
Packer images
Ansible/Chef/Puppet
provider-native resources
CI/CD deployment tools
```

---

### 33. Complex Expressions

#### `flatten`

Turns nested lists into one list.

```hcl
flatten([[80, 443], [8080]])
```

Result:

```hcl
[80, 443, 8080]
```

#### `setproduct`

Creates all combinations.

```hcl
setproduct(["dev", "uat"], ["westus2", "eastus"])
```

Result:

```hcl
[
  ["dev", "westus2"],
  ["dev", "eastus"],
  ["uat", "westus2"],
  ["uat", "eastus"]
]
```

#### `lookup`

Map lookup with default.

```hcl
lookup(local.sizes, var.environment, "Standard_B1s")
```

#### `try`

Returns first expression that does not error.

```hcl
port = app.port
```

#### `can`

Tests whether an expression succeeds.

```hcl
can(regex("^[a-z0-9]+$", var.name))
```

#### `coalesce`

Returns first non-null/non-empty value.

```hcl
name = coalesce(var.custom_name, "default-name")
```

---

### 34. Complex Expression Example

Non-null optional defaults require Terraform 1.3+. try catches evaluation errors, not null values; defaults in the type definition handle omitted and explicit null attributes here.

Input:

```hcl
variable "apps" {
  type = map(object({
    regions = list(string)
    port    = optional(number, 80)
    tags    = optional(map(string), {})
  }))

  default = {
    api = {
      regions = ["westus2", "eastus"]
      port    = 8080
    }

    worker = {
      regions = ["westus2"]
    }
  }
}
```

Transform:

```hcl
locals {
  app_region_pairs = flatten([
    for app_name, app in var.apps : [
      for region in app.regions : {
        name   = app_name
        region = region
        port   = app.port
        tags   = app.tags
      }
    ]
  ])

  deployments = {
    for item in local.app_region_pairs :
    "${item.name}-${item.region}" => item
  }
}
```

Result:

```hcl
{
  "api-westus2" = {
    name   = "api"
    region = "westus2"
    port   = 8080
    tags   = {}
  }

  "api-eastus" = {
    name   = "api"
    region = "eastus"
    port   = 8080
    tags   = {}
  }

  "worker-westus2" = {
    name   = "worker"
    region = "westus2"
    port   = 80
    tags   = {}
  }
}
```

Purpose:

```text
Input: apps with multiple regions
Output: one deployment per app per region
```

---

### 35. Policy and Security Scanning

Common tools:

```text
terraform fmt
terraform validate
TFLint
Checkov
Trivy config
tfsec
OPA/Conftest
Sentinel
Azure Policy
```

Pipeline flow:

```text
terraform fmt -check
terraform init
terraform validate
tflint
trivy config/checkov
terraform plan -out=tfplan
terraform show -json tfplan > tfplan.json
conftest/checkov plan scan
approval
terraform apply tfplan
```

Policy-as-code examples:

```text
deny Key Vault without purge protection
deny NSG public SSH
require tags
require private endpoints
block public storage access
```

OPA/Conftest checks plan JSON using Rego.

Sentinel is HashiCorp's policy framework for Terraform Cloud/Enterprise.

---

## GitHub Actions

### 1. Workflow Permissions

Example:

```yaml
permissions:
  contents: write
  security-events: write
  packages: write
  actions: read
  attestations: write
  id-token: write
```

Meaning:

```text
contents: write         = update repo contents/tags/releases
security-events: write  = upload code scanning/SARIF results
packages: write         = publish packages/images to GHCR
actions: read           = read workflow/action metadata
attestations: write     = create artifact provenance/attestations
id-token: write         = request OIDC token
```

Interview answer:

> Permissions define what the job's GITHUB_TOKEN can do. I grant least privilege per job instead of broad default permissions.

---

### 2. `GITHUB_TOKEN` vs PAT

`secrets.GITHUB_TOKEN` is automatically generated by GitHub Actions for each workflow run.

It is:

```text
temporary
repo-scoped
controlled by workflow permissions
not your personal token
```

PAT:

```text
personal or service account token
longer-lived
stored in secrets
permissions depend on token scopes
```

Example:

```yaml
password: ${{ secrets.GITHUB_TOKEN }}
```

This uses the automatic workflow token, not your own token.

---

### 3. `github.actor`

```yaml
username: ${{ github.actor }}
```

Means:

```text
Use the account that triggered the workflow.
```

Could be:

```text
human user
dependabot[bot]
github-actions[bot]
service account
```

Prefer github.actor with GITHUB_TOKEN for same-repository GHCR publishing. Use a narrowly scoped GitHub App token or PAT only when cross-repository access requires it. An alternative credential pair is:

```yaml
username: ${{ vars.DEVOPS_USER }}
password: ${{ secrets.DEVOPS_TOKEN }}
```

---

### 4. GitHub Actions Variables and Secrets

Variables:

```yaml
GH_ACTOR: ${{ vars.DEVOPS_USER }}
```

Use for non-secret config.

Secrets:

```yaml
GH_TOKEN: ${{ secrets.DEVOPS_TOKEN }}
```

Use for sensitive values.

`GH_TOKEN` is recognized by GitHub CLI:

```bash
gh api ...
gh release create ...
```

---

### 5. Reusable Workflows: `workflow_call`

Reusable workflow:

```yaml
on:
  workflow_call:
    inputs:
      java-version:
        required: true
        type: string
    secrets:
      DEVOPS_TOKEN:
        required: true
```

Called at job level:

```yaml
jobs:
  CI-CD:
    uses: org/repo/.github/workflows/App-CI-CD.yml@main
    with:
      java-version: "25"
    secrets:
      DEVOPS_TOKEN: ${{ secrets.DEVOPS_TOKEN }}
```

`workflow_call` means:

```text
This workflow can be called by another workflow.
```

---

### 6. Composite Actions

Composite action:

```yaml
runs:
  using: "composite"
  steps:
    - shell: bash
      run: echo "Build Docker image"
```

Called at step level:

```yaml
steps:
  - uses: org/action-repo@v1
```

Difference:

```text
Reusable workflow:
  file: .github/workflows/*.yml
  has: on: workflow_call
  called at job level

Composite action:
  file: action.yml
  has: runs: using: composite
  called at step level
```

---

### 7. Pinning by SHA

Example:

```yaml
uses: org/repo/.github/workflows/App-CI-CD.yml@6d6245a3eeb5c7aa7d118a1a74be9c047d009047
```

The value after `@` is a commit SHA.

Meaning:

```text
Use the workflow exactly as it existed at that commit.
```

Benefits:

```text
reproducibility
supply-chain security
no surprise changes from moving branch/tag
```

---

### 8. Docker Login Action

Example:

```yaml
- name: Log in to the Container registry
  uses: docker/login-action@65b78e6e13532edd9afa3aa52ac7964289d1a9c1
  with:
    registry: ${{ inputs.registry }}
    username: ${{ github.actor }}
    password: ${{ inputs.token }}
```

Meaning:

```text
registry = container registry like ghcr.io
username = account that triggered workflow
password = token passed into action
```

If:

```yaml
token: ${{ secrets.GITHUB_TOKEN }}
```

then the password is GitHub's temporary workflow token, not your personal token.

---

### 9. CodeQL Init

Example:

```yaml
- name: Initialize CodeQL
  uses: github/codeql-action/init@<sha>
  with:
    languages: ${{ inputs.code-QL-language }}
    build-mode: ${{ inputs.code-QL-language == 'java' && 'autobuild' || 'none' }}
    config: |
      paths-ignore:
        - lib
        - tests
      queries:
        - uses: security-extended
        - uses: security-and-quality
```

Meaning:

```text
initialize CodeQL analysis
choose language from input
use autobuild for Java
path exclusions depend on language and build mode; for Java autobuild, exclude files from the build itself
run extended security and quality queries
```

Flow:

```text
CodeQL init
build/autobuild
CodeQL analyze
upload security findings
```

---

### 10. Trivy Threshold Script

Example:

```bash
CRITICAL_COUNT=$(jq '[.Results[].Vulnerabilities[]?.Severity | select(. == "CRITICAL")] | length' "$FILE")
HIGH_COUNT=$(jq '[.Results[].Vulnerabilities[]?.Severity | select(. == "HIGH")] | length' "$FILE")
```

Meaning:

```text
read Trivy JSON
count vulnerabilities by severity
```

Threshold check:

```bash
if [ "$CRITICAL_COUNT" -gt "$CRITICAL_THRESHOLD" ]; then
  FAIL_REASON="${FAIL_REASON:+$FAIL_REASON; }CRITICAL ($CRITICAL_COUNT) > $CRITICAL_THRESHOLD"
fi
```

Final failure:

```bash
if [ -n "$FAIL_REASON" ]; then
  echo "Vulnerability threshold(s) exceeded: $FAIL_REASON"
  exit 1
fi
```

Meaning:

```text
If any severity count exceeds threshold, fail the workflow.
```

---

### 11. Artifact Directory Flattening

Prefer setting the download action destination explicitly. The legacy snippet below misses dotfiles, fails for empty directories, and can overwrite files; do not use it as a general-purpose extraction script.

Example:

```bash
if [ -d "./$ARTIFACT_NAME" ]; then
  mv ./$ARTIFACT_NAME/* ./
  rm -r ./$ARTIFACT_NAME
else
  echo "Artifact directory not found or artifact structure is different."
fi
```

Meaning:

```text
If artifact directory exists:
  move files from artifact folder into current directory
  delete empty artifact folder
else:
  print warning
```

Used after downloading artifacts when later steps expect files in the current directory.

---

### 12. Git Config URL Rewrite for Private Terraform Modules

This explains an existing pattern, not a recommended default. URL rewrites can persist credentials in Git configuration. Prefer a short-lived GitHub App token or a read-only SSH deploy key, an isolated runner, and cleanup. Never interpolate untrusted inputs into shell commands.

Example:

```yaml
- name: Terraform init
  run: |
    git config --global url."https://${{ secrets.DEVOPS_TOKEN }}:@github.com/".insteadOf "https://github.com/"
    terraform init
```

Meaning:

```text
When Git tries https://github.com/...
rewrite it to include DEVOPS_TOKEN
```

Used so `terraform init` can download private GitHub modules.

---

### 13. Terraform Variables from GitHub Actions

Example:

```yaml
env:
  TF_VAR_github_username: ${{ secrets.GHCR_USERNAME }}
  TF_VAR_github_pat: ${{ secrets.DEVOPS_TOKEN }}
```

Terraform automatically maps:

```text
TF_VAR_github_username -> var.github_username
TF_VAR_github_pat      -> var.github_pat
```

`var.github_pat` is a placeholder in Terraform.

`TF_VAR_github_pat` provides the runtime value.

---

### 14. GitHub Actions Concurrency

Example:

```yaml
concurrency:
  group: terraform-dev-state
  cancel-in-progress: false
```

Meaning:

```text
Only one job/run in this repository group runs at a time.
By default one pending run is retained; newer arrivals replace that pending run.
Backend state locking is still needed across local runs and other repositories.
```

Use for Terraform state:

```yaml
dev-plan:
  concurrency:
    group: terraform-dev-state
    cancel-in-progress: false
```

Best practice:

```text
same state file = same concurrency group
different state files = different concurrency groups
```

For Terraform, prefer:

```yaml
cancel-in-progress: false
```

to avoid canceling an apply mid-run.

---

### 15. Azure Login with OIDC

Typical pattern:

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - name: Azure Login
    uses: azure/login@<reviewed-full-commit-sha>
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

`id-token: write` allows GitHub Actions to request an OIDC token.

This supports passwordless/federated auth to Azure instead of storing a client secret.

---

### 16. GitHub Actions Interview Answer

Strong answer:

> In GitHub Actions, I pay close attention to triggers, permissions, tokens, environment protections, concurrency, and artifact flow. I use least-privilege `permissions`, prefer OIDC to cloud secrets, pin reusable workflows/actions by SHA, distinguish reusable workflows from composite actions, use concurrency for Terraform state safety, and treat artifacts/plan files as sensitive when they may contain secrets.

---

## Final Advanced Terraform Interview Answer

If asked what makes someone advanced in Terraform:

> Advanced Terraform is not just knowing more syntax. It is understanding state, resource addresses, provider configuration, dependency graphs, CI/CD plan/apply safety, drift, locking, imports, moved blocks, sensitive state, and how to avoid accidental replacement or state corruption in production.

If asked how to handle unexpected replace/destroy:

> I first inspect the plan to identify the exact replacement reason. Then I check whether it is a real immutable change, a resource address change, a provider/subscription mismatch, or missing/wrong state. I use `state list`, `state show`, config comparison, and Azure resource IDs to verify. If the resource exists but is missing from state, I import it. If the Terraform address changed, I use a `moved` block or `state mv`. If Terraform should stop managing it without deleting it, I use `state rm`. I avoid blindly applying destroy/create plans, especially for critical resources.



## Reference documentation

- [Terraform type constraints and optional defaults](https://developer.hashicorp.com/terraform/language/expressions/type-constraints)
- [GitHub Actions concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
- [CodeQL workflow configuration](https://docs.github.com/en/code-security/reference/code-scanning/workflow-configuration-options)
