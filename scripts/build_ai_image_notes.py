"""Recreate the twenty supplied study-note photographs as one accessible HTML page.

The photographed text is transcribed below; diagrams are rebuilt as native SVG.
Source photographs remain in the user's Downloads folder and are not published.
"""
from pathlib import Path
from html import escape
import json
import textwrap
from ai_notes_enrichment import enrich, diffusion_svg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/generative-ai'
PAGES = []

def page(number, title, source):
    item = {'page': number, 'title': title, 'sourceFile': source, 'blocks': []}
    PAGES.append(item)
    return item['blocks']

def h(title): b.append({'type': 'heading', 'text': title})
def p(text): b.append({'type': 'paragraph', 'text': text})
def li(*items): b.append({'type': 'list', 'items': list(items)})
def table(headers, *rows): b.append({'type': 'table', 'headers': headers.split('|'), 'rows': [r.split('|') for r in rows]})
def code(text, language='text'): b.append({'type': 'code', 'language': language, 'text': textwrap.dedent(text).strip()})
def note(text): b.append({'type': 'note', 'text': text})
def flow(title, *layers, edges=None):
    # Each layer is a row of nodes; explicit edges permit branches and feedback.
    b.append({'type': 'diagram', 'title': title, 'layers': [list(x) if isinstance(x, tuple) else [x] for x in layers], 'edges': edges})

b = page(1, 'Generative AI — Complete Developer Study Notes', '1792805787192.jpeg')
p('Concepts • Practical Examples • Projects • Interview Preparation')
p('20 pages, recreated as one HTML learning page with 20 subsections.')
note('Reading guide: the photographed notes are organized in their printed page order. Text, comparison tables, formulas, code and diagram labels are recreated below. Blue clarification boxes distinguish editorial corrections from the supplied notes. Model names, tools, dimensions, scores and outputs in the notes are study examples, not a current product catalogue or measured results. The original photos are not embedded.')
flow('Complete developer learning path', 'Foundations and model types', 'Prompts, tokens and embeddings', 'Transformers, attention and training', 'Agents, retrieval and evaluation', 'Security, adaptation and system design', 'Interview questions and final revision')

b = page(2, 'Introduction to Generative AI', '1792805788662.jpeg')
h('1.1 What is Generative AI?')
li('Generative AI refers to a class of AI models that can generate new content such as text, images, audio, video and code based on patterns learned from existing data.', 'Instead of just predicting a label or class, it learns the underlying distribution of data and generates new, similar but original outputs.', 'It can understand context, follow instructions and create human-like content.')
h('1.2 Examples of Generated Content')
table('Content|Examples', 'Text|Articles, summaries, chat responses', 'Images|Realistic images, artwork, design', 'Audio|Speech, music, voice cloning', 'Video|Video generation, animation', 'Code|Complete programs, documentation')
h('1.3 How Does Generative AI Work?')
li('It learns the patterns and structure from a large amount of data.', 'It models the probability distribution of data.', 'During inference, it samples from this distribution to generate new content.', 'Modern models such as Transformers are trained on massive datasets using self-supervised learning.')
h('1.4 Key Characteristics')
li('Learns from large and diverse datasets.', 'Generates new and original content.', 'Can follow natural language instructions.', 'Works across multiple modalities: text, image, audio, video and code.', 'Shows emergent capabilities with scale.', 'Can be fine-tuned for specific use cases.')
h('1.5 Generative AI vs Traditional AI')
table('Aspect|Traditional AI (Discriminative)|Generative AI (Generative)', 'Goal|Predict a label or category|Generate new content', 'Output|Fixed set of labels (classification)|Open-ended, creative output', 'Learning|Learns decision boundary|Learns data distribution', 'Examples|Spam detection, image classification|Text generation, image generation', 'Typical Models|Logistic Regression, SVM, CNN|Transformers, Diffusion Models, GANs, VAEs', 'Use Cases|Analysis, prediction, detection|Content creation, design, automation')
h('1.6 High-Level Architecture of Generative AI')
flow('From prompt to generated content', 'Input (Prompt)', 'Tokenizer\nConvert text to tokens', 'Embedding Layer\nToken representations', 'Generative Model\nTransformer / Diffusion / GAN', 'Output (Generated Content)\nText / Image / Audio / Video / Code')
note('The source repeats the label 1.1 for Key Characteristics; it is numbered 1.4 here. The tokenizer/embedding pipeline is a text-model illustration: image, audio, diffusion and GAN pipelines do not all share this exact sequence. Generated content can reproduce training material and must still be checked.')

b = page(3, 'Types of Generative AI Models', '1792805788708.jpeg')
h('2.1 Major Types of Generative AI Models')
p('Generative AI models can be broadly classified based on their architecture and learning approach. Each type has its own strengths, use cases and applications.')
li('Large Language Models (LLMs)', 'Diffusion Models', 'Generative Adversarial Networks (GANs)', 'Variational Autoencoders (VAEs)', 'Autoregressive Models', 'Multimodal Models')
h('2.2 Comparison of Model Types')
table('Model Type|Key Idea|Common Use Cases', 'LLMs|Predict next token based on context|Text generation, chatbots, summarization', 'Diffusion Models|Denoise data step by step|Image, video, audio generation', 'GANs|Generator vs Discriminator|Realistic image generation, data synthesis', 'VAEs|Learn latent representation|Image generation, anomaly detection', 'Autoregressive Models|Model sequential distribution|Text, speech, time series', 'Multimodal Models|Work with multiple input modalities|Text + Image, Text + Audio, Text + Video')
h('2.3 Large Language Models (LLMs)')
li('Based on Transformer architecture.', 'Trained on massive text data using self-supervised learning.', 'Learn to predict the next token in a sequence.', 'Examples in the notes: GPT, LLaMA, Claude, Gemini, Mistral.')
flow('Language-model generation', 'Input Prompt', 'Tokenizer\nText → Tokens', 'Transformer Model\nProcess using attention layers', 'Next Token Prediction\nGenerate next token')
h('2.4 Diffusion Models')
li('Learn to generate data by gradually removing noise from a random input.', 'Work in two processes: forward (add noise) and reverse (denoise).', 'Excellent for high-quality image and video generation.', 'Examples in the notes: Stable Diffusion, DALL·E (diffusion based), Imagen, Sora.')
flow('Diffusion: denoising progression', 'Random Noise', 'Step 1 (denoise)', 'Step 2 (denoise)', 'Step n (Generated Image)')
h('2.5 Generative Adversarial Networks (GANs)')
li('Consist of two neural networks: Generator creates fake data; Discriminator distinguishes real vs fake data.', 'Both networks are trained together in a competitive manner: adversarial training.', 'Widely used for realistic image generation.', 'Examples: DCGAN, StyleGAN, BigGAN.')
flow('GAN: real and generated samples', ('Random Noise (z)', 'Real Data (x)'), 'Generator (G)\nGenerate Fake Samples', 'Fake Data G(z)', 'Discriminator (D)\nReal or Fake?', edges=[[[0,0],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],[[0,1],[3,0]]])
h('2.6 Variational Autoencoders (VAEs)')
li('Learn a compressed latent representation of data.', 'Consist of an Encoder and a Decoder.', 'Encoder maps input to a probability distribution: mean and variance.', 'Decoder generates data by sampling from latent space.', 'Useful for image generation, anomaly detection and data compression.', 'Examples: VAE, β-VAE, VQ-VAE.')
flow('VAE: encode, sample and reconstruct', 'Input (x)', 'Encoder q(z|x)\nMean (μ), Variance (σ²)', 'z (Latent space)', 'Decoder p(x|z)', 'Reconstructed Output (x̂)')
h('2.7 Autoregressive Models')
li('Model the joint probability of data as a product of conditional probabilities.', 'Generate data token by token in a sequential manner.', 'Widely used in text, speech and time-series generation.', 'Examples: GPT (autoregressive), PixelRNN, WaveNet.')
h('2.8 Multimodal Generative AI Models')
li('Work with multiple input and output modalities: text, image, audio, video.', 'Can understand and generate content across different formats.', 'Examples in the notes: DALL·E (text to image), GPT-4V (text + image), LLaVA, Gemini (multimodal).')
note('These groups overlap: an LLM can be autoregressive and multimodal. The named model versions are examples from the source. Denoising is shown as labeled stages rather than the tiny cat photographs. VQ-VAE uses a discrete codebook; it is not identical to a Gaussian-latent VAE.')

b = page(4, 'LLM Fundamentals', '1792805788229.jpeg')
h('3.1 What is a Large Language Model (LLM)?')
li('An LLM is a type of generative AI model trained on massive text data to understand, generate and manipulate human language.', 'It learns the probability distribution of the next token given the previous tokens.', 'LLMs are based on the Transformer architecture and use a self-attention mechanism.', 'Examples in the notes: GPT, LLaMA, Claude, Gemini, Mistral.')
h('3.2 How LLMs Generate Text')
li('LLMs generate text token by token.', 'Given an input prompt, the model predicts the next token using learned patterns from training data.', 'This process repeats until an end condition is met.', 'Decoding strategies such as greedy search, beam search or sampling select the next token.')
flow('Repeated next-token generation', 'Input Prompt\n“Explain Generative AI”', 'LLM (Transformer)\nGenerate next token repeatedly', 'Output\n“Generative AI is a type of …”')
h('3.3 Tokenization')
li('Tokenization converts text into smaller units called tokens: words, subwords or characters.', 'LLMs use subword tokenization techniques to handle rare words and reduce vocabulary size.', 'Common tokenizers: BPE (Byte Pair Encoding), SentencePiece, WordPiece.')
code('Text: “Generative AI is amazing”\nTokens (illustrative): [“Gener”, “ative”, “AI”, “is”, “amaz”, “ing”]')
h('3.4 Tokenization Example (BPE)')
table('Step|Text|Tokens (Example)', '1|Generative|[Gener, ative]', '2|AI|[AI]', '3|is|[is]', '4|amazing|[amaz, ing]', 'Final|Generative AI is amazing|[Gener, ative, AI, is, amaz, ing]')
h('3.5 Transformer Architecture (Overview)')
li('LLMs are based on Transformer architecture, which uses self-attention instead of RNNs.', 'The model consists of multiple decoder layers for GPT-like models, or encoder-decoder layers for models such as T5.', 'Each layer contains self-attention and feed-forward neural networks.')
flow('Transformer: decoder-only overview (e.g. GPT)', 'Input Text', 'Tokenization', 'Token Embedding', 'Positional Encoding', 'Decoder Layer (N×)\nMasked Self-Attention', 'Add & Layer Norm', 'Feed Forward Network', 'Add & Layer Norm', 'Linear + Softmax', 'Next Token Probabilities')
h('3.6 Key Components of an LLM')
table('Component|Purpose', 'Tokenizer|Convert text to tokens', 'Embedding Layer|Convert tokens to dense vectors', 'Positional Encoding|Add position information to tokens', 'Transformer Layers|Learn context using self-attention', 'Feed Forward Network|Non-linear transformation of features', 'Layer Normalization|Stabilize training and improve performance', 'Output Layer|Convert hidden states to token probabilities')
h('3.7 Next Token Prediction (Mathematical View)')
p('LLMs model the conditional probability of a sequence. During inference, the model predicts the next token xₜ₊₁ based on previous tokens x₁, x₂, …, xₜ. A linear layer produces vocabulary logits and softmax produces probabilities.')
code('P(x₁, x₂, …, xₙ) = ∏ᵢ₌₁ⁿ P(xᵢ | x₁, x₂, …, xᵢ₋₁)\n\nP(xₜ₊₁ = w) = exp(z_w) / Σᵥ∈V exp(z_v)')
note('z_w is the logit for vocabulary token w, not the hidden state itself as the source shorthand suggests. Greedy decoding selects the highest-probability token; sampling need not. The layer diagram shows the source’s simplified post-normalization layout; exact layouts vary by architecture.')

b = page(5, 'Prompt Engineering', '1792805788525.jpeg')
h('4.1 What is Prompt Engineering?')
li('Prompt engineering is the process of designing effective input prompts to get the desired, high-quality output from a generative AI model such as ChatGPT, Claude or Gemini.', 'It helps in controlling the model’s behavior, style, format and level of detail.', 'A well-crafted prompt can improve accuracy, relevance and consistency of responses.', 'It is an important skill for developers, product builders and AI engineers.')
h('4.2 Anatomy of a Good Prompt')
flow('Good Prompt = Instruction + Context + Input + Output Format', 'Good Prompt', ('Instruction\nWhat to do? (Clear task)', 'Context\nBackground (domain, role)', 'Input\nData or specific details', 'Output Format\nList, table, code, explanation'))
h('4.3 Prompting Techniques')
table('Technique|Description', 'Zero-Shot Prompting|Give only a task instruction.', 'Few-Shot Prompting|Provide a few examples in the prompt.', 'Chain-of-Thought (CoT) Prompting|The source suggests asking the model to think step by step.', 'Role Prompting|Assign a specific role to the model.', 'Instruction Prompting|Clearly specify the task and format.', 'Self-Consistency|Generate multiple answers and pick the best one.', 'Tree of Thoughts (ToT)|Explore multiple reasoning paths (advanced).')
h('4.4 Examples of Prompts')
table('Type|Prompt|Use Case', 'Zero-Shot|Explain quantum computing in simple words.|Basic question', 'Few-Shot|Classify the sentiment: “I love this!” → Positive; “This is bad” → Negative; “Amazing experience” → ?|Classification tasks', 'Chain-of-Thought|Solve this step by step: If a car travels 120 km in 2 hours, what is the speed?|Reasoning and math', 'Role Prompting|You are a Java expert. Explain microservices architecture in simple terms.|Domain-specific questions', 'Instruction|Summarize the following text in 5 bullet points: [paste text]|Summarization')
h('4.5 Prompting Styles and Use Cases')
table('Style|Description|Example Use Cases', 'Direct|Simple and clear instruction|Quick answers, definitions', 'Detailed|Provide context, constraints and format|Complex explanation, code generation', 'Comparative|Ask to compare multiple options|Pros and cons, decision making', 'Creative|Generate imaginative and original content|Stories, marketing content, ideas', 'Technical|Use domain-specific instructions|Code, system design, debugging', 'Structured|Ask for output in a specific format|JSON, table, bullet points')
h('4.6 Prompt Template (Reusable)')
code('''You are a {role}.
Your task is to {instruction}.
Context:
{provide background information}
Input:
{provide input data or question}
Please provide the output in {format}.
Constraints:
- {constraint 1}
- {constraint 2}
- {constraint 3}''')
h('4.7 Real Example (Code Generation)')
code('''You are a senior Java developer.
Write a Spring Boot REST API to create a user with name, email and mobile number.
Use proper validation and return a meaningful response.
Provide complete code with controller, service and model classes.''')
flow('Prompt → LLM → generated code', 'Prompt: Spring Boot user API', 'LLM\nChatGPT, Claude, etc.', 'Output\nUser entity class; Repository interface\nService class; Controller class\nSample request and response; Validation logic')
h('4.8 Best Practices')
li('Be clear and specific.', 'Provide necessary context.', 'Use examples when needed.', 'Specify the desired output format.', 'Iterate and refine the prompt.', 'Use role and constraints.', 'Break complex tasks into smaller steps.')
note('Ask for a concise explanation, assumptions, calculations and checks that can be inspected; private internal reasoning is not a dependable interface. Self-consistency requires a selection or voting criterion and independent validation; agreement alone does not prove correctness. A role prompt does not grant authority or expertise.')

b = page(6, 'Tokenization and Embeddings', '1792805788835.jpeg')
h('5.1 What is Tokenization?')
li('Tokenization converts text into smaller units called tokens: words, subwords or characters.', 'It helps the model process text data.', 'Modern LLMs use subword tokenization techniques to handle rare words and reduce vocabulary size.', 'The same text can be tokenized differently depending on the tokenizer and model.')
h('5.2 Types of Tokenization')
table('Type|Description|Example', 'Word Tokenization|Split text into words|“AI is amazing” → [AI, is, amazing]', 'Character Tokenization|Split into characters|“AI” → [A, I]', 'Subword Tokenization|Split into subwords (common in LLMs)|“unbelievable” → [un, believable]', 'Byte Pair Encoding (BPE)|Merges frequent subword units|“low” + “er” → “lower”', 'SentencePiece|Unsupervised, language-agnostic tokenizer tooling|Used in models such as LLaMA, T5, Gemini in the notes', 'WordPiece|Used in BERT models|“playing” → [play, ##ing]')
h('5.3 Byte Pair Encoding (BPE) — How It Works')
li('1. Start with character-level tokens.', '2. Find the most frequent pair of tokens.', '3. Merge the pair into a new token.', '4. Repeat until the desired vocabulary size is reached.')
code('''Example: build a vocabulary for “lowest”.
Step 1: l o w e s t  (characters)
Step 2: illustrative intermediate state: lo we st
Step 3: merge again: low est
Final tokens: [low, est]''')
h('5.4 Tokenization Example (Python)')
code('''from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
text = "Generative AI is amazing!"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(tokens)
print(token_ids)
# Example printed in the source (illustrative, not a verified run):
# ['Generative', 'ĠAI', 'Ġis', 'Ġamazing', '!']
# [34390, 2277, 318, 19801, 0]''', 'python')
h('5.5 What are Embeddings?')
li('Embeddings are dense vector representations of tokens in a high-dimensional space.', 'They capture semantic meaning and context of words.', 'Tokens with similar meaning can have similar embeddings.', 'Embeddings are learned during model training.', 'Embeddings help the model understand relationships between words.')
h('5.6 Embedding Layer')
li('Converts token IDs into dense vectors of fixed size: embedding dimension.', 'Each token ID maps to a trainable vector.', 'The embedding layer is a lookup table of size vocabulary size × embedding dimension.', 'These vectors are later used as input to the Transformer model.')
flow('Embedding lookup', 'Token IDs\n[101, 2054, 2003]', 'Embedding Layer\nV × D\nV = vocabulary size; D = embedding dimension', 'Embedding Vectors\nShape: [3, D]\n[0.12, −0.03, …]\n[0.45, 0.22, …]\n[−0.11, 0.09, …]')
h('5.7 Example of Embeddings')
p('Word embeddings in 3D space for visualization. Example relation from the notes: King − Man ≈ Queen − Woman. This illustrates semantic relationships; it is not guaranteed for every model.')
b.append({'type':'scatter', 'title':'Illustrative embedding space: King, Man, Woman and Queen'})
h('5.8 Embedding vs One-Hot Encoding')
table('Aspect|One-Hot Encoding|Embeddings', 'Representation|Sparse vector (0/1)|Dense vector (real numbers)', 'Dimension|Very high (vocabulary size)|Lower (e.g. 768, 1536)', 'Sparsity|Very sparse|Dense', 'Semantic meaning|Does not capture similarity directly|Captures semantic relationships', 'Memory usage|High in a dense representation|Lower per vector', 'Performance|Not efficient as a dense vector|Efficient and widely used in LLMs')
note('BPE learns pair frequencies over a training corpus, not by choosing convenient merges in a single word. The “lowest” stages are schematic. Token IDs and exact output depend on the tokenizer vocabulary; run the example to inspect actual output. SentencePiece is tooling that can train BPE or unigram tokenizers. Static token embeddings become contextual representations after Transformer layers. Sparse one-hot vectors need not be stored densely.')

b = page(7, 'Transformer Architecture for Generative AI', '1792805788783.jpeg')
h('6.1 Why Transformers?')
li('RNNs and LSTMs process data sequentially, which is slow and inefficient for long sequences.', 'Transformers use self-attention to process tokens in parallel.', 'They can capture long-range dependencies.', 'Transformers have become a foundation of modern generative AI models such as GPT, LLaMA and BERT.')
p('Key idea: self-attention instead of recurrence.')
h('6.2 Overall Transformer Architecture')
flow('Encoder (e.g. BERT) vs Decoder (e.g. GPT)', ('Encoder input\nToken embeddings', 'Decoder input\nShifted right'), ('Multi-Head Attention', 'Masked Multi-Head\nSelf-Attention'), ('Add & Layer Norm', 'Add & Layer Norm'), ('Feed Forward Network', 'Feed Forward Network'), ('Add & Layer Norm\nRepeat N×', 'Add & Layer Norm\nRepeat N×'), ('Encoded Representations', 'Next Token Probabilities'), edges=[[[r,c],[r+1,c]] for r in range(5) for c in range(2)])
h('6.3 Transformer vs RNN/LSTM')
table('Aspect|RNN / LSTM|Transformer', 'Processing|Sequential|Parallel during training', 'Memory|Hidden state|Self-attention', 'Long-range dependencies|Difficult|Handles well', 'Training speed|Slower|Faster parallel execution', 'Architecture|Recurrent|Attention based', 'Used in|Earlier models|Modern LLMs')
h('6.4 Encoder vs Decoder (for Generative AI)')
table('Encoder (used in BERT, T5)|Decoder (used in GPT, LLaMA)', 'Reads the entire input sequence|Generates text token by token', 'Uses self-attention|Uses masked self-attention (causal attention)', 'Generates contextual representations (embeddings)|Looks only at previous tokens and itself', 'Used for understanding text: classification, QA, etc.|Outputs probability distribution for next token')
h('6.5 Transformer Decoder Block (Detailed)')
flow('Decoder block with residual connections', 'Input (X)', 'Masked Multi-Head Self-Attention\nLooks at previous tokens and itself', 'Residual Add + Layer Norm', 'Feed Forward Network\nLinear d_model → d_ff\nReLU / GELU\nLinear d_ff → d_model', 'Residual Add + Layer Norm', 'Output (X′)', edges=[[[0,0],[1,0]],[[1,0],[2,0]],[[0,0],[2,0]],[[2,0],[3,0]],[[3,0],[4,0]],[[2,0],[4,0]],[[4,0],[5,0]]])
h('6.6 Causal Masking (Important for Generation)')
li('In a decoder, each token can only attend to previous tokens and itself, not future tokens.', 'This is achieved with a causal mask: an upper-triangular matrix containing −∞ above the diagonal.', 'It prevents the model from seeing future tokens during training and inference.')
code('''Attention mask (length = 5)
[ 0  −∞  −∞  −∞  −∞ ]
[ 0   0  −∞  −∞  −∞ ]
[ 0   0   0  −∞  −∞ ]
[ 0   0   0   0  −∞ ]
[ 0   0   0   0   0 ]''')
h('6.7 Complete Forward Pass (High Level)')
flow('Text to next-token probabilities', 'Input Text', 'Tokenization', 'Token Embeddings + Positional Encoding', 'N × Decoder Blocks', 'Linear + Softmax', 'Next Token Probabilities')
h('6.8 Key Takeaways')
li('Transformers use self-attention to capture context.', 'A decoder uses causal masking for text generation.', 'Multi-head attention helps learn multiple patterns.', 'Residual connections and layer normalization stabilize training.', 'Transformer architecture is a foundation of modern generative AI models.')
note('Parallel training does not make autoregressive generation parallel across all output tokens. T5 has both an encoder and a decoder; its decoder also attends to encoder outputs. BERT is primarily an encoder model, not an autoregressive text generator. Modern decoder normalization and positional methods may differ from the simplified diagram.')

b = page(8, 'Self-Attention Mechanism', '1792805788749.jpeg')
h('7.1 What is Self-Attention?')
li('Self-attention allows the model to look at tokens in the input sequence and identify which tokens are important for each token.', 'It helps capture long-range dependencies in a single layer.', 'It computes attention scores between tokens using Query (Q), Key (K) and Value (V) vectors.', 'Self-attention is a core building block of Transformers and is used in encoders and decoders.')
h('7.2 Intuition')
li('For each token, compute how much it should attend to each permitted token in the sequence.', 'Tokens that are more relevant get higher attention scores.', 'The output is a weighted sum of value vectors based on attention weights.')
h('7.3 Self-Attention Workflow')
flow('Scaled dot-product self-attention', 'Input Tokens (X)\n[n, d_model]', 'Linear Projections\nQ = XW^Q; K = XW^K; V = XW^V', 'Compute Attention Scores\nQKᵀ', 'Scale the Scores\nQKᵀ / √d_k', 'Apply Softmax\nAttention Weights (A)', 'Weighted Sum of Values\nOutput = AV')
h('7.4 Dimensions')
table('Matrix|Shape|Description', 'Input X|[n, d_model]|Input token embeddings', 'Query Q|[n, d_k]|Query vectors', 'Key K|[n, d_k]|Key vectors', 'Value V|[n, d_v]|Value vectors', 'Attention Scores QKᵀ|[n, n]|Similarity between tokens', 'Attention Weights A|[n, n]|After softmax', 'Output AV|[n, d_v]|Contextualized token vectors')
h('7.5 Mathematical Formulation')
code('''Q = XW^Q       K = XW^K       V = XW^V
Scores = QKᵀ
Scaled scores = QKᵀ / √d_k
A = softmax(QKᵀ / √d_k)       # row-wise
Output = AV''')
p('Scaling by √d_k prevents very large dot products from pushing softmax into extreme saturation. Apply any causal/padding mask before softmax.')
h('7.6 Self-Attention Diagram')
flow('Queries and keys determine weights; values carry content', 'Input X [n, d_model]', ('Linear W^Q\nQ [n, d_k]', 'Linear W^K\nK [n, d_k]', 'Linear W^V\nV [n, d_v]'), 'QKᵀ → Scale 1/√d_k → Softmax\nA [n, n]', 'MatMul: A × V', 'Output [n, d_v]', edges=[[[0,0],[1,c]] for c in range(3)]+[[[1,0],[2,0]],[[1,1],[2,0]],[[2,0],[3,0]],[[1,2],[3,0]],[[3,0],[4,0]]])
h('7.7 Example (Simple Sentence)')
p('Input: “The cat sat on the mat”. Tokens: [The, cat, sat, on, the, mat].')
table('Token|Important Tokens it Attends To (Illustrative)', 'The|cat, mat', 'cat|The, sat', 'sat|cat, on', 'on|sat, the, mat', 'the|The, mat', 'mat|The, on')
h('7.8 Key Takeaways')
li('Self-attention allows tokens to attend to one another in parallel.', 'It captures long-range dependencies.', 'It uses Query, Key and Value vectors.', 'It uses scaled dot-product attention with softmax.', 'Output is a weighted sum of value vectors.', 'It is a core component of models such as GPT, LLaMA and BERT.')
note('The example attention relationships are illustrative, not measured attention weights. In a causal decoder, future-token edges in this unmasked example are forbidden. The source workflow labels the final shape [n, d_k]; the general correct shape is [n, d_v], which only equals it when d_v = d_k.')

b = page(9, 'Multi-Head Attention', '1792805788745.jpeg')
h('8.1 What is Multi-Head Attention?')
li('Multi-head attention runs multiple attention mechanisms, or heads, in parallel.', 'Each head learns different relationships between tokens.', 'It allows the model to capture diverse patterns such as syntactic, semantic and positional information.', 'Outputs from all heads are concatenated and projected to a single output.', 'It improves the model’s ability to represent complex context.')
h('8.2 Intuition')
li('Instead of a single attention head, multiple heads view input from different perspectives.', 'Some heads may capture grammatical relationships, some coreference, and some long-range dependencies.', 'Finally, all heads are combined into a richer representation.')
h('8.3 Multi-Head Attention Architecture')
flow('Parallel heads and final projection', 'Input X\n[n, d_model]', ('Head 1 Attention', 'Head 2 Attention', '… Head h Attention'), 'Concatenate\n[n, h × d_v]', 'Linear Projection W^O\n[n, d_model]', 'Output\n[n, d_model]')
h('8.4 Computation Steps')
code('''1. Project input to Query, Key and Value for each head:
   Qᵢ = XWᵢ^Q    Kᵢ = XWᵢ^K    Vᵢ = XWᵢ^V
2. Compute attention for each head:
   headᵢ = Attention(Qᵢ, Kᵢ, Vᵢ)
3. Concatenate all heads:
   MultiHead = Concat(head₁, head₂, …, head_h)
4. Apply output linear projection:
   Output = MultiHead W^O''')
h('8.5 Detailed Diagram with Dimensions')
flow('Multi-head projections with tensor dimensions', 'Input X\n[n, d_model]', ('Linear W^Q\n[n, h × d_k]', 'Linear W^K\n[n, h × d_k]', 'Linear W^V\n[n, h × d_v]'), ('Split Q into h heads\n[n, h, d_k]', 'Split K into h heads\n[n, h, d_k]', 'Split V into h heads\n[n, h, d_v]'), 'Scaled Dot-Product Attention (each head)\n[n, h, d_v]', 'Concatenate Heads\n[n, h × d_v]', 'Linear W^O\n[n, h × d_v] → [n, d_model]', 'Output\n[n, d_model]', edges=[[[0,0],[1,c]] for c in range(3)]+[[[1,c],[2,c]] for c in range(3)]+[[[2,c],[3,0]] for c in range(3)]+[[[r,0],[r+1,0]] for r in range(3,6)])
h('8.6 Example with Dimensions')
p('Assume n = 10 (sequence length), d_model = 512, h = 8 (number of heads). Then d_k = d_v = d_model / h = 512 / 8 = 64.')
table('Step|Shape|Description', 'Input X|[10, 512]|Input token embeddings', 'Q, K, V after linear|[10, 512]|Projected representations', 'Split into heads|[10, 8, 64]|8 heads with dimension 64', 'Attention output|[10, 8, 64]|Output for all heads; one head is [10, 64]', 'Concatenate heads|[10, 512]|Concatenate 8 heads: 8 × 64', 'Final linear projection|[10, 512]|Project back to d_model')
h('8.7 Why Multiple Heads?')
li('Different heads can focus on different parts of the sequence.', 'Capture multiple types of relationships: local, global, syntactic and semantic.', 'Improve model performance.', 'Help represent complex language structures.')
h('8.8 Key Takeaways')
li('Multi-head attention runs multiple attention heads in parallel.', 'Each head learns a different representation.', 'Outputs are concatenated and projected.', 'It helps capture richer and more diverse context.', 'It is a key component of Transformer architecture.')
note('Dimensions omit the batch axis. Implementations often arrange tensors as [batch, heads, sequence, dimension]. The notes use d_k for concatenated output; d_v is the general value dimension. The common example sets them equal. Head specialization is possible, not a guaranteed human-interpretable role for every head.')

b = page(10, 'Positional Encoding', '1792805788725.jpeg')
h('9.1 Why Positional Encoding?')
li('Self-attention without position information cannot distinguish word order by itself.', 'Without positional information, the model cannot understand token order in a sequence.', 'Positional encoding adds information about each token’s position to its embedding vector.', 'It helps the model distinguish token positions and capture meaning based on word order.')
h('9.2 Intuition')
li('Each token is assigned a positional vector based on its position in the sequence.', 'This vector is added to the token embedding in the original Transformer formulation.', 'The resulting input contains token meaning from the embedding and position information.')
h('9.3 Overall Flow')
flow('Add position to token meaning', 'Input Tokens\n[“The”, “cat”, “sat”]', 'Token Embeddings\n[n, d_model]', 'Positional Encoding\n[n, d_model]', 'Add (Element-wise)\nToken Embedding + Positional Encoding', 'Input to Transformer\n[n, d_model]')
h('9.4 Formula (Sinusoidal Positional Encoding)')
code('''PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))

pos = token position: 0, 1, 2, …
i = frequency-pair index: 0, 1, 2, …
d_model = embedding dimension, e.g. 512''')
h('9.5 Example Calculation')
p('Assume d_model = 4 and a sequence of 3 tokens at positions 0, 1 and 2.')
table('Position|PE(pos, 0)|PE(pos, 1)|PE(pos, 2)|PE(pos, 3)', '0|sin(0) = 0|cos(0) = 1|sin(0) = 0|cos(0) = 1', '1|sin(1)|cos(1)|sin(1/100)|cos(1/100)', '2|sin(2)|cos(2)|sin(2/100)|cos(2/100)')
h('9.6 Positional Encoding Matrix')
code('''For n = 3 and d_model = 4:
PE = [ 0        1        0             1            ]
     [ sin(1)   cos(1)   sin(1/100)    cos(1/100)   ]
     [ sin(2)   cos(2)   sin(2/100)    cos(2/100)   ]''')
h('9.7 Adding to Token Embeddings')
code('''Final input to the model = Token Embedding + Positional Encoding
X = E + PE
E:  [n, d_model] token embeddings
PE: [n, d_model] positional encoding
X:  [n, d_model] input to Transformer''')
h('9.8 Visual Representation')
code('''Token Embeddings (E)       Positional Encoding (PE)       Transformer Input (X)
[e₁₁ e₁₂ e₁₃ e₁₄]       [p₁₁ p₁₂ p₁₃ p₁₄]          [x₁₁ x₁₂ x₁₃ x₁₄]
[e₂₁ e₂₂ e₂₃ e₂₄]   +   [p₂₁ p₂₂ p₂₃ p₂₄]    =     [x₂₁ x₂₂ x₂₃ x₂₄]
[e₃₁ e₃₂ e₃₃ e₃₄]       [p₃₁ p₃₂ p₃₃ p₃₄]          [x₃₁ x₃₂ x₃₃ x₃₄]
Each matrix has shape [n, d_model].''')
h('9.9 Learnable vs Sinusoidal Positional Encoding')
table('Aspect|Sinusoidal (Original)|Learnable (Alternative)', 'Type|Fixed (not trainable)|Trainable parameters', 'Formula|Sine and cosine|Learned embeddings', 'Generalization|Can compute positions beyond training length|May not generalize to longer sequences', 'Usage|Original Transformer|Used in models such as BERT and GPT variants', 'Performance|Works well|Sometimes better; task dependent')
h('9.10 Key Takeaways')
li('Positional encoding provides token-position information.', 'It is added to token embeddings in this formulation.', 'Sinusoidal encoding uses sine and cosine functions.', 'It helps the model represent token order.', 'Position information is a crucial component of Transformer models.')
note('More precisely, unmasked self-attention without position signals is permutation-equivariant, not permutation-invariant. Modern models may use rotary or relative position methods instead of adding absolute position vectors. Being able to compute a longer sinusoidal sequence does not guarantee reliable extrapolation.')

b = page(11, 'Model Training and Fine-Tuning', '1792805788825.jpeg')
h('10.1 Pre-training vs Fine-tuning')
table('Aspect|Pre-training|Fine-tuning', 'Purpose|Learn general language understanding|Adapt to a specific task or domain', 'Data|Large and diverse text data, e.g. web|Smaller, task-specific dataset', 'Objective|Next-token prediction for causal LMs; self-supervised learning|Task-specific objective, e.g. classification or summarization', 'Model|Base model, e.g. GPT, LLaMA, BERT|Pre-trained model further trained', 'Compute|Very high|Relatively lower', 'Output|General-purpose model|Domain/task-specialized model')
h('10.2 Pre-training Process')
li('Use large-scale unlabeled text data.', 'Convert text into tokens and embeddings.', 'Train using next-token prediction for causal language modeling.', 'Learn general patterns, grammar, reasoning patterns and world knowledge.')
flow('Pre-training with backpropagation', 'Large Text Corpus\nBooks, web, wiki', 'Tokenization + Embeddings', 'Transformer Model', 'Next Token Prediction (Loss)', 'Update Model Parameters\nBackpropagation', edges=[[[0,0],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],[[3,0],[4,0]],[[4,0],[2,0]]])
h('10.3 Next Token Prediction Objective')
p('Given a sequence of tokens x₁, x₂, …, xₙ, the model learns to maximize the probability of the next token.')
code('L = −(1/n) Σᵢ₌₁ⁿ log P(xᵢ | x₁, x₂, …, xᵢ₋₁)')
li('The probability is computed using a softmax over the vocabulary.', 'The model is trained to minimize the loss: negative log likelihood.')
h('10.4 Training Steps')
li('1. Prepare and clean a large text dataset.', '2. Tokenize the text.', '3. Convert tokens to embeddings with positional information.', '4. Pass through the Transformer model.', '5. Compute loss using next-token prediction.', '6. Update parameters using an optimizer such as AdamW.', '7. Repeat over the training data for the planned training budget.')
h('10.5 Fine-tuning Process')
li('Start with a pre-trained model.', 'Use a smaller, task-specific dataset.', 'Continue training on new data, often for a few epochs.', 'The model adapts to the task while aiming to retain general knowledge.', 'Fine-tune all parameters or only a subset, e.g. LoRA.')
flow('Fine-tuning a pre-trained model', ('Pre-trained Model\nLLaMA, GPT', 'Task-Specific Dataset\nQA, summarization'), 'Fine-tuning\nContinue Training', 'Adapted Model')
h('10.6 Fine-tuning Techniques')
table('Technique|Description|Parameters Updated|Use Case', 'Full Fine-tuning|Update all model parameters|All|High-quality results, more compute', 'Parameter-Efficient Fine-tuning (PEFT)|Update a small set of parameters|Adapters, prefixes, etc.|Efficient fine-tuning', 'LoRA|Low-Rank Adaptation; adds small matrices|Only LoRA parameters|Popular and efficient', 'QLoRA|LoRA with 4-bit quantization|Only LoRA parameters|Memory-efficient adaptation of large models', 'Prompt Tuning|Learn soft prompts instead of full model|Only prompt embeddings|Very efficient')
h('10.7 LoRA (Low-Rank Adaptation)')
li('Instead of updating the full weight matrix W, LoRA adds small low-rank matrices.', 'Only the low-rank factors are trained; they contain far fewer parameters.')
code('''Original weight: W ∈ ℝ^(d×k)
LoRA update: W′ = W + ΔW = W + ABᵀ
A ∈ ℝ^(d×r), B ∈ ℝ^(k×r), r ≪ min(d, k)
Equivalent factor notation: ΔW = A B_factor, B_factor ∈ ℝ^(r×k).''')
flow('Frozen weights plus a trainable low-rank update', 'Input X', ('Pre-trained Weight W\nFrozen', 'LoRA Update\nA (d × r) · Bᵀ (r × k)'), 'Add: W + ΔW', 'Output')
h('10.8 Key Takeaways')
li('Pre-training teaches general language patterns.', 'Fine-tuning adapts a model to a task or domain.', 'Next-token prediction is the causal-LM training objective.', 'Parameter-efficient methods such as LoRA and QLoRA are widely used.', 'Fine-tuning usually requires less data and compute than pre-training.', 'It can improve performance for real-world applications.')
note('The source mixes ABᵀ with dimensions for AB. The factors above make both notations dimensionally consistent. BERT uses masked language modeling rather than causal next-token prediction. More epochs are not automatically better: monitor held-out quality and forgetting; multiple passes over a huge corpus are not required in every pre-training run.')

b = page(12, 'Tokenization Methods and Vocabulary', '1792805788803.jpeg')
h('11.1 What is Tokenization?')
li('Tokenization converts raw text into smaller units called tokens.', 'Tokens can be words, subwords, characters or byte-based units.', 'Tokens map to unique integer IDs using a vocabulary.', 'This helps the model process text efficiently.')
h('11.2 Why Tokenization is Needed')
li('Computers and models operate on numeric representations of text.', 'Converts text into numeric form.', 'Handles unseen words using subword techniques.', 'Reduces vocabulary size compared with storing every possible word.', 'Helps handle different languages, typos and new words.')
h('11.3 Types of Tokenization')
table('Type|Example|Pros|Cons', 'Word level|“The cat” → [The, cat]|Simple, interpretable|Large vocabulary, unknown words', 'Character level|“cat” → [c, a, t]|Handles any covered character|Very long sequences', 'Subword level: BPE, WordPiece, Unigram|“playing” → [play, ing]|Good balance; handles new words|More complex than word level', 'Byte level|“cat” → [99, 97, 116]|Works for any encoded text, including emojis|Longer sequences before merges')
h('11.4 Word-Level Tokenization Example')
p('Sentence: “The cat sat on the mat”. Split by space → [The, cat, sat, on, the, mat]. Map to IDs using a vocabulary.')
table('Token|ID (Example from Source)', 'The|10', 'cat|25', 'sat|30', 'on|18', 'the|10', 'mat|45')
h('11.5 Subword Tokenization (Byte Pair Encoding — BPE)')
li('Start with characters as the initial vocabulary.', 'Find the most frequent pair of tokens.', 'Merge the pair into a new token.', 'Repeat for a fixed number of merges.', 'This creates subword units that can handle new words.')
code('''Training words: [lower, lowest, newer, wider]
1. Start with characters: [l, o, w, e, r, s, t, n, i, d]
2. Example frequent pair: (l, o) → lo
3. Next example merge: (lo, w) → low
4. Continue …
Illustrative final splits printed in the source:
“lower”  → [low, er]
“newer”  → [new, er]
“widest” → [wide, st]''')
h('11.6 Vocabulary and Token IDs')
li('Each vocabulary token has a fixed integer ID.', 'The collection of tokens is called a vocabulary.', 'Example vocabulary size: 8.')
table('Token|ID', '<pad>|0', '<unk>|1', 'The|2', 'cat|3', 'sat|4', 'on|5', 'mat|6', '.|7')
flow('Vocabulary lookup', 'Tokenized Sequence\n“The cat sat .”', 'Map tokens to vocabulary IDs', '[2, 3, 4, 7]')
h('11.7 Special Tokens')
table('Token|Purpose', '<pad>|Padding to equal sequence lengths', '<unk>|Unknown token, not in vocabulary', '<bos>|Beginning of sequence', '<eos>|End of sequence', '<sep>|Separator between sentences in some models', '<mask>|Masked language modeling, e.g. BERT')
h('11.8 Key Takeaways')
li('Tokenization converts text into tokens.', 'Subword tokenization such as BPE, WordPiece and Unigram is common in modern LLMs.', 'A vocabulary maps each token to a unique ID.', 'Special tokens help model training and inference.', 'Tokenization is crucial for handling diverse and unseen words.')
note('The source assigns both “The” and “the” to ID 10 in its first table. That requires normalization such as lowercasing; a case-sensitive tokenizer normally treats them separately. The BPE merges and final splits are schematic, not a learned vocabulary verified from the four listed words. Special-token names and presence vary by tokenizer.')

b = page(13, 'AI Agents and Tool Use', '1792805788846.jpeg')
h('12.1 What are AI Agents?')
li('AI agents use LLMs to interpret a goal, plan steps, use tools and take actions to complete tasks.', 'Unlike a simple LLM chat, an agent can interact with external tools, APIs, databases and files.', 'Agents can plan, take multiple steps and adapt based on results.', 'Agents are useful for automation, research, data analysis and other multi-step tasks.')
h('12.2 Key Components of an AI Agent')
flow('Agent components', 'User Goal / Query', ('Agent\nLLM + Orchestration', 'Tools\nAPIs, DB, Files, Internet, Code'), 'Planner\nSteps and task plan', 'Memory\nConversation, Context, Past Results', 'Final Output\nAnswer / Action Taken', edges=[[[0,0],[1,0]],[[1,0],[1,1]],[[1,1],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],[[3,0],[4,0]]])
h('12.3 Types of AI Agents')
table('Type|Description|Example Use Case', 'Simple Agent|Single-step action|Use a calculator for a math query', 'ReAct Agent|Reason and act iteratively|Search internet, read results, answer', 'Tool-Using Agent|Use external tools/APIs|Call weather API, fetch data from DB', 'Planning Agent|Break task into steps and execute|Plan a travel itinerary', 'Autonomous Agent|Works with minimal human input|Research, analyze data, create report')
h('12.4 How an Agent Works (Flow)')
flow('Bounded agent workflow', '1. Understand User Goal\nLLM interprets intent', '2. Plan Steps\nBreak down into small tasks', '3. Select and Use Tools\nCall APIs, search, read files, run code', '4. Observe Results\nGet output from tools', '5. Iterate\nIf needed, refine steps and repeat', '6. Final Answer\nReturn response to user', edges=[[[r,0],[r+1,0]] for r in range(5)]+[[[4,0],[2,0]]])
h('12.5 Example: Agent for Travel Planning')
p('User query: “Plan a 3-day trip to Goa from Delhi including flights, hotels and places to visit.”')
flow('Travel-planning agent', 'User Query', ('Agent (LLM)', 'Tools\nFlight API; Hotel API\nSearch (Places); Maps API'), 'Plan\n1. Search Flights\n2. Search Hotels\n3. Find Places to Visit', 'Call Tools and Get Results', 'Combine Information and Generate Itinerary', 'Final Output\n3-day Plan', edges=[[[0,0],[1,0]],[[1,0],[1,1]],[[1,1],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],[[3,0],[4,0]],[[4,0],[5,0]]])
h('12.6 Common Tools Used by Agents')
table('Tool Type|Examples|Purpose', 'Web Search|Google Search, Tavily|Get latest information', 'APIs|Weather API, Flight API|Fetch real-time data', 'Databases|MySQL, MongoDB|Read/write data', 'File System|Read/write files|Work with local files', 'Code Execution|Python REPL|Run code, calculations', 'Knowledge Base|Vector DB, e.g. Qdrant|Retrieve domain knowledge', 'Custom Tools|Any business API|Domain-specific actions')
h('12.7 Example: ReAct-Style Agent (Pseudocode)')
code('''User: “What is the current weather in Delhi?”
Plan summary: A weather API is needed for live data.
Action: get_weather_api(city="Delhi")
Observation (illustrative): {"city":"Delhi", "temp":28, "condition":"Clear"}
Result summary: Use the observed API response to answer.
Final Answer: “The current weather in Delhi is 28°C with clear skies.”''')
h('12.8 Key Takeaways')
li('AI agents use LLMs to plan and take actions.', 'They can use external tools such as APIs, databases and files.', 'A ReAct-style loop alternates planning, action and observation.', 'Different agents fit different use cases.', 'Tools and memory make agents more capable.', 'Examples include travel planning, automation, research and data analysis.')
note('The source’s “Thought” lines are rendered as inspectable plan/result summaries; they are not private model reasoning or proof of correctness. The weather is example data, not a live report. Tool permissions, input validation, iteration limits and approval for sensitive actions must be enforced by application code.')

b = page(14, 'RAG — Retrieval-Augmented Generation', '1792805788697.jpeg')
h('13.1 What is RAG?')
li('RAG combines information retrieval with text generation.', 'It fetches relevant information from external knowledge sources such as documents and databases and provides it to the LLM as context.', 'This can help generate more accurate, up-to-date and domain-specific answers.', 'RAG can reduce hallucinations and allow use of private or organizational data.')
h('13.2 Why RAG is Needed')
li('LLMs have limited training knowledge and a bounded context window.', 'They may generate incorrect or hallucinated answers.', 'RAG uses information from external sources.', 'Useful for enterprise data, documentation, Q&A systems and customer support.')
h('13.3 RAG Architecture (High Level)')
flow('High-level retrieval-augmented generation', 'User Query', 'Query Embedding', 'Vector Search (Retrieval)', 'Relevant Documents (Top K)', 'Combine Context\nPrompt Engineering', 'LLM (Generation)', 'Final Output\nAnswer with Sources')
h('13.4 RAG Workflow (Detailed Steps)')
table('Step|Stage|What Happens', '1|Load Data|Ingest PDF, docs, web and database documents.', '2|Chunking|Split documents into smaller chunks, e.g. 500 tokens with overlap.', '3|Create Embeddings|Convert each chunk into a vector using an embedding model.', '4|Store in Vector DB|Save embeddings and metadata, e.g. Qdrant or Pinecone.', '5|Retrieve|Embed a user query and find top-K similar chunks.', '6|Augment Prompt|Combine retrieved chunks with the query using a prompt template.', '7|Generate Answer|Send augmented prompt to LLM; return the answer with sources.')
h('13.5 Data Ingestion and Chunking')
li('Load data from sources such as PDF, web and database.', 'Split documents into smaller chunks for retrieval.', 'Use overlap between chunks to maintain context.')
flow('Chunking with 50-token overlap', 'Original Text\nLarge Document', 'Split into Chunks\nchunk_size = 500 tokens\noverlap = 50 tokens', ('Chunk 1\nTokens 1–500', 'Chunk 2\nTokens 451–950', 'Chunk 3\nTokens 901–1400'))
h('13.6 Embeddings and Vector Database')
li('Convert each chunk into a high-dimensional embedding vector using an embedding model.', 'Similar chunks can have similar vector representations.', 'Store vectors in a vector database for similarity search.')
table('Component|Description|Examples from Notes', 'Embedding Model|Converts text to vector|all-MiniLM-L6-v2, OpenAI, BGE', 'Vector Database|Stores and searches vectors|Qdrant, Pinecone, Weaviate, FAISS', 'Similarity Search|Finds relevant chunks using vector similarity|Cosine Similarity, Dot Product')
h('13.7 Retrieval and Generation')
li('Convert the user query into an embedding vector.', 'Retrieve top-K relevant chunks using similarity search.', 'Add retrieved context to the prompt.', 'Send the augmented prompt to the LLM to generate the answer.')
flow('Retrieval and generation path', 'User Query', 'Query Embedding', 'Vector DB\nSimilarity Search', 'Top K Chunks', 'Augmented Prompt\nQuery + Retrieved Context', 'LLM (Generation)', 'Final Answer\nCitations / Sources')
h('13.8 Benefits and Use Cases')
table('Aspect|Details', 'Accuracy|Can provide factual, up-to-date answers', 'Reduced Hallucination|Uses documents rather than relying only on learned knowledge', 'Domain Specific|Works with private/organizational data', 'Scalability|Can handle large document collections', 'Flexibility|Works with PDFs, DB, web and other data sources', 'Use Cases|Chat with documents, internal Q&A, customer support, research assistants, knowledge management')
note('RAG does not guarantee truth or authorization. Enforce document access before retrieval, validate sources and freshness, treat retrieved text as untrusted data, and allow “not enough evidence.” FAISS is a similarity-search library, not a complete managed database. Chunk size and overlap here are examples to evaluate, not universal defaults.')

b = page(15, 'Vector Databases and Semantic Search', '1792805788918.jpeg')
h('14.1 What is a Vector Database?')
li('A vector database stores, indexes and searches high-dimensional vectors or embeddings.', 'It enables similarity search over unstructured data such as text and images.', 'It focuses on vector similarity rather than only exact keyword matches.', 'It is used in RAG, recommendation systems, image search and AI applications.')
h('14.2 Why Vector Databases are Needed')
li('Traditional keyword search can miss meaning and context.', 'Embeddings convert data into numerical vectors.', 'Vector indexes support similarity search over millions of vectors.', 'They can use indexing algorithms such as HNSW, IVF and PQ.', 'Useful for semantic search, RAG, chatbots and recommendations.')
h('14.3 Vector Representation')
flow('Text to a vector representation', 'Text\n“The cat sits”', 'Embedding Model\nall-MiniLM, OpenAI, etc.', 'Vector\n[0.12, −0.34, 0.56, 0.21, …]\n768 dimensions (example)')
h('14.4 Example Embeddings')
table('Text|Vector (5 dimensions, illustrative)', '“The cat”|[0.10, 0.23, −0.11, 0.45, 0.08]', '“A dog”|[0.12, 0.20, −0.10, 0.40, 0.07]', '“Car”|[−0.50, 0.10, 0.60, −0.20, 0.30]')
h('14.5 Similarity Search')
li('Finds vectors most similar to a query vector.', 'Common metrics: cosine similarity, Euclidean distance and dot product.')
table('Metric|Formula|Range|Use Case', 'Cosine Similarity|cos(θ) = (A · B) / (‖A‖ ‖B‖)|−1 to 1 for nonzero vectors|Common for text', 'Euclidean Distance|d(A, B) = √Σᵢ(Aᵢ − Bᵢ)²|0 to ∞|General purpose; lower is closer', 'Dot Product|A · B = Σᵢ AᵢBᵢ|−∞ to ∞|Used in some embedding models')
h('14.6 Vector Database Workflow')
flow('Index documents and retrieve similar chunks', 'Documents\nText, PDF, Web', '1. Split into Chunks\nSmaller pieces, e.g. 500 tokens', '2. Generate Embeddings\nEmbedding model converts each chunk', '3. Store in Vector DB\nVectors + metadata', '4. Query Embedding\nSearch for similar chunks', '5. Retrieve Top K Similar Chunks\nRank by similarity score')
h('14.7 Popular Vector Databases')
table('Database|Type in Notes|Key Features in Notes|Use Cases', 'Pinecone|Managed (Cloud)|Scalable, easy to use, low latency|RAG, semantic search, AI apps', 'Weaviate|Open Source|Hybrid vector + keyword search, GraphQL|RAG, knowledge graphs, AI apps', 'Qdrant|Open Source|Fast search, filtering, payload support|RAG, search, recommendations', 'Milvus|Open Source|Distributed, large-scale, high performance|Enterprise, large datasets', 'Chroma|Open Source|Simple, lightweight, good for prototyping|RAG, local apps, learning')
h('14.8 Example: Semantic Search')
p('Query: “Best places to visit in Goa”. Query embedding q = [0.21, −0.11, 0.33, …].')
table('Document|Illustrative Vector|Illustrative Score', '1. Goa travel guide|[0.20, −0.10, 0.31, …]|0.95', '2. Best beaches in India|[0.15, −0.05, 0.28, …]|0.87', '3. Himalayan treks|[−0.30, 0.40, −0.12, …]|0.12')
p('Top result: Document 1, with the highest illustrative similarity score.')
h('14.9 Metadata Filtering (Hybrid Search)')
li('Vector databases can filter using metadata such as category, date and source.', 'This helps retrieve more relevant results.')
table('Chunk|Text|Metadata', '1|Goa travel guide|{"category":"travel","location":"Goa"}', '2|Delhi food guide|{"category":"food","location":"Delhi"}', '3|Java tutorial|{"category":"education","topic":"Java"}')
p('Query: “travel places in Goa” + filter: category = travel.')
h('14.10 Key Takeaways')
li('Vector databases enable similarity search over embeddings.', 'They use efficient indexing techniques such as HNSW, IVF and PQ.', 'They support metadata filtering; some support hybrid search.', 'Useful for RAG, recommendations and AI applications.', 'Examples include Pinecone, Weaviate, Qdrant, Milvus and Chroma.', 'Choose based on scalability, features and the use case.')
note('The incomplete vectors and scores are illustrative and cannot be recomputed from the shown coordinates. Metadata filtering is not the same as hybrid ranking, which typically combines lexical and vector search. Authorization filters must come from trusted identity context. Product features and hosting options listed here reflect the source examples; verify them before selecting a product.')

b = page(16, 'Evaluation and Hallucination Control', '1792805788803 (1).jpeg')
h('15.1 Why Evaluation is Important')
li('LLMs can generate fluent but incorrect answers.', 'We need to evaluate quality, relevance, accuracy and safety.', 'Evaluation helps compare models, prompts and RAG strategies.', 'Essential for chatbots, enterprise search and AI agents.', 'It supports more reliable AI systems.')
h('15.2 What is Hallucination?')
li('A hallucination is incorrect or fabricated information not supported by facts or context.', 'It may sound believable while being wrong.', 'Common in knowledge questions, numbers, citations and domain-specific answers.', 'RAG, prompting and evaluation can help reduce hallucinations.')
h('15.3 Types of Hallucinations')
table('Type|Description|Example of an Incorrect Answer', 'Factual Hallucination|Incorrect facts or fake information|“Taj Mahal was built in 1600” — incorrect year', 'Contextual Hallucination|Not aligned with given context|Answering about a different topic', 'Citation Hallucination|Fake references|“According to Smith (2020)…” when no such reference exists', 'Numerical Hallucination|Incorrect numbers or calculations|“India has 5 billion people” — incorrect', 'Logical Hallucination|Illogical or contradictory statements|Claims that violate basic logic')
h('15.4 Evaluation Metrics')
table('Metric|Description|Use Case', 'Accuracy|Correctness of answer|General QA', 'Faithfulness|Grounded in provided context|RAG, factual QA', 'Relevance|Answers the actual question|Search, chatbots', 'Context Precision|Relevance of retrieved chunks|RAG retrieval', 'Context Recall|Coverage of necessary sources|RAG retrieval', 'F1 Score|Balance of precision and recall|Task-specific evaluation', 'BLEU / ROUGE|Traditional text-overlap measures|Summarization and generation', 'BERTScore|Semantic similarity using embeddings|Model evaluation', 'RAGAS|RAG evaluation framework|RAG applications')
h('15.5 RAGAS Evaluation Framework')
li('RAGAS is a framework for evaluating RAG systems.', 'It provides metrics for retrieval quality, answer quality and faithfulness.', 'Used for testing and benchmarking RAG pipelines.')
table('Metric in Notes|Description', 'Context Precision|How relevant retrieved chunks are', 'Context Recall|How many relevant chunks were retrieved', 'Faithfulness|Whether the answer is grounded in context', 'Answer Relevancy|How relevant the answer is to the question', 'Answer Correctness|Overall correctness of the final answer')
h('15.6 Techniques to Control Hallucinations')
li('Use RAG with trusted, up-to-date sources.', 'Provide clear and specific instructions.', 'Use structured output formats such as JSON or tables.', 'Add citations/source references.', 'Use lower temperature for factual tasks when supported.', 'Validate answers using external tools or APIs.', 'Apply guardrails and content filters.', 'Use function calling or tools to fetch real-time data.')
h('15.7 RAG with Citation Example')
flow('Evidence-grounded answer with citations', 'User Query', 'Retrieve Relevant Documents (RAG)', 'Generate Answer with Citations', 'Final Output\nAnswer + Sources')
code('''Query: “What is the capital of France?”
Retrieved Context: [Doc1: “Paris is the capital of France …”]
LLM Answer: “The capital of France is Paris.”
Citations printed in the source example:
[1] Europe Travel Guide (2023)
[2] Wikipedia — France (2024)''')
h('15.8 Best Practices')
li('Consider RAG for domain-specific or private data when retrieval fits the task.', 'Evaluate answers using multiple metrics, including semantic similarity and task checks.', 'Show sources/citations to users.', 'Keep prompts clear and avoid ambiguous questions.', 'Use metadata filtering to retrieve relevant documents.', 'Continuously monitor and evaluate outputs.', 'Implement guardrails to detect harmful or incorrect content.')
h('15.9 Key Takeaways')
li('Evaluation is essential for reliable AI applications.', 'Hallucinations are common and can be reduced, not eliminated by one technique.', 'Use RAG, clear prompts, citations and evaluation metrics.', 'Tools such as RAGAS help measure RAG performance.', 'Validate important answers against trusted sources.')
note('Low temperature can reduce output variation; it does not make an answer true. A citation must identify an actually retrieved source and support the associated claim. The two source labels in the example are placeholders, not verified references. Metric names and definitions vary by framework version. Human review and task-specific checks remain necessary, especially when an LLM grades another LLM.')

b = page(17, 'Security, Cost and Performance in Generative AI', '1792805788849.jpeg')
h('16.1 Why It is Important')
li('Generative AI applications may process sensitive data and can be expensive to run.', 'We need data security, privacy, cost control and good performance.', 'These concerns help build reliable, safe and scalable applications.', 'They matter for enterprise adoption and production environments.')
h('16.2 Security Risks in Generative AI')
table('Risk|Description', 'Data Leakage|Sensitive data exposed in prompts or outputs', 'Prompt Injection|Malicious prompts try to manipulate model behavior', 'Model Jailbreak|Techniques to bypass safety restrictions', 'Insecure Plugins/Tools|External tools introduce security risks', 'Data Privacy|User data may be stored or used for training depending on service terms', 'Adversarial Attacks|Crafted inputs induce harmful or incorrect outputs')
h('16.3 Security Best Practices')
li('Do not send sensitive or confidential data to unapproved systems.', 'Use data masking and anonymization where appropriate.', 'Implement input validation and output/content checks.', 'Use role-based access control for applications.', 'Log and monitor prompts and responses with appropriate redaction and access controls.', 'Use HTTPS, authentication and secure API endpoints.', 'Regularly test prompt injection and jailbreak attempts.', 'Address applicable privacy and compliance requirements, such as the GDPR/HIPAA examples in the notes.')
h('16.4 Cost Factors in Generative AI')
table('Factor|Description', 'Model Usage|Input/output token charges', 'Model Size|Larger models often require more compute', 'Inference Type|Real-time inference vs batch processing', 'Context Length|Longer contexts increase input token usage', 'Fine-tuning|Training compute costs', 'Infrastructure|GPU/CPU instances, storage and network', 'Third-party Services|API credits or subscriptions', 'Data Storage|Documents, embeddings and logs')
h('16.5 Cost Optimization Strategies')
li('Use smaller, efficient models when quality permits; source examples include GPT-3.5 and LLaMA.', 'Cache repeated queries with correct authorization boundaries.', 'Use vector retrieval to select relevant context.', 'Optimize prompts to be short and clear.', 'Use batch processing for non-real-time work.', 'Consider quantization for self-hosted deployment.', 'Monitor token usage and set limits/quotas.', 'Choose cloud or self-hosted infrastructure to fit the task.')
h('16.6 Performance Metrics')
table('Metric|Description|Goal', 'Latency|Time to get a response|Lower is better', 'Throughput|Requests per second|Higher within quality/error targets', 'Token Processing Speed|Generated tokens per second|Higher within quality targets', 'Accuracy / Quality|Relevance and correctness|Higher is better', 'Resource Usage|CPU, GPU, memory utilization|Efficient usage', 'Availability|Uptime of service|Target such as 99.9%, per application', 'Scalability|Handle increasing load|Scale smoothly')
h('16.7 Performance Optimization Techniques')
li('Use quantization such as 8-bit or 4-bit to reduce memory usage.', 'Use GPU acceleration where beneficial.', 'Cache frequent queries, e.g. Redis.', 'Stream responses to reduce perceived latency.', 'Optimize prompt length and remove unnecessary context.', 'Consider inference frameworks such as vLLM, TensorRT and ONNX.', 'Use load balancing and autoscaling for high traffic.', 'Monitor and profile regularly.')
h('16.8 Example Architecture (Secure and Scalable)')
flow('Secure and scalable application architecture', 'User (Frontend)', 'API Gateway\nAuth, Rate Limit, Input Validation', 'Application\nLLM + RAG', ('LLM\nProvider / self-hosted', 'Vector DB\nEmbeddings', 'Cache\nRedis'), 'Secure Storage\nEncrypted Data', 'Monitoring & Logging\nELK / Prometheus / Grafana')
h('16.9 Key Takeaways')
li('Security, cost and performance are critical for real-world applications.', 'Protect data and prevent misuse.', 'Use cost and performance optimization techniques.', 'Continuously monitor, evaluate and improve.', 'Choose tools and infrastructure based on the use case and requirements.')
note('The source’s model names and token billing unit are historical examples, not pricing guidance. Never rely on a prompt as an access-control boundary: enforce tenant and resource permissions in the application and tools. Logs and caches also need isolation and retention controls. Encryption and filtering alone do not establish compliance; this page is a technical study outline, not legal guidance.')

b = page(18, 'Fine-Tuning and Adaptation Techniques', '1792805788874.jpeg')
h('17.1 What is Fine-Tuning?')
li('Fine-tuning means further training a pre-trained LLM on a smaller, domain-specific dataset.', 'It can teach domain patterns, a specific style and task behavior.', 'It may improve accuracy and consistency for a measured task.', 'Use cases include customer support, code generation, legal documents and medical Q&A in the notes.')
h('17.2 Types of Model Adaptation')
table('Type|Description|Use Case', 'Full Fine-Tuning|Update all parameters|High performance with sufficient data and compute', 'Parameter-Efficient Fine-Tuning (PEFT)|Update a small set of parameters|Cost-effective adaptation', 'LoRA (Low-Rank Adaptation)|Add small trainable matrices|Efficient adaptation of large models', 'QLoRA|LoRA with 4-bit quantization|Lower memory use', 'Instruction Tuning|Train on instruction-response data|Better instruction following', 'Domain Adaptation|Fine-tune on domain-specific data|Enterprise/industry use cases')
h('17.3 Full Fine-Tuning vs LoRA')
table('Aspect|Full Fine-Tuning|LoRA / QLoRA', 'Parameters Updated|All parameters|Small adapter parameter set', 'Memory Requirement|Very high|Lower', 'Training Time|High|Often lower; depends on setup', 'Cost|Expensive|Often more cost-effective', 'Performance|Strong with sufficient data|Can work well with less data', 'Use Case|Advanced, large dataset|Many resource-constrained adaptation tasks')
h('17.4 Fine-Tuning Process (Steps)')
flow('Fine-tuning from dataset to monitored deployment', '1. Prepare Dataset\nInstruction, input-output pairs', '2. Preprocess Data\nCleaning, formatting, tokenization', '3. Choose Fine-Tuning Method\nFull, LoRA, QLoRA, etc.', '4. Train the Model\nFrameworks such as Hugging Face', '5. Evaluate Model\nHeld-out dataset and metrics', '6. Deploy and Monitor\nCloud or local')
h('17.5 Training Data Format (Example)')
p('Commonly used format in the notes: instruction-input-output JSONL. Each training record occupies one line in a JSONL file.')
code('''{"instruction":"Summarize the given text","input":"Large Language Models are powerful …","output":"Large Language Models (LLMs) are AI models trained on massive text data to understand and generate human-like text."}''', 'json')
h('17.6 Popular Frameworks and Tools')
table('Tool / Framework|Purpose|Features Listed in Notes', 'Hugging Face Transformers|Model training and fine-tuning|Full fine-tuning and integration with PEFT/LoRA/QLoRA', 'PEFT (Hugging Face)|Parameter-efficient fine-tuning|LoRA, prefix tuning, adapter methods', 'TRL (Hugging Face)|Post-training / RLHF and SFT|Supervised fine-tuning and reinforcement-learning tooling', 'DeepSpeed|Large-scale training|Memory optimization, distributed training', 'BitsAndBytes|4-bit and 8-bit quantization|Lower memory usage', 'Unsloth|Faster fine-tuning workflows|Optimized supported LLM training, LoRA/QLoRA')
h('17.7 Fine-Tuning Architecture')
flow('Domain adaptation architecture', 'Domain Dataset\nInstructions, Q&A, Documents', 'Data Preprocessing\nCleaning and Formatting', 'Tokenization\nUsing model tokenizer', ('Pre-trained LLM\nLLaMA, Mistral, Phi, Gemma', 'Fine-Tuning\nLoRA / QLoRA / Full'), 'Trained Model\nDomain Specific', 'Evaluation\nAccuracy, Relevance', 'Deployment\nAPI / Application', edges=[[[0,0],[1,0]],[[1,0],[2,0]],[[2,0],[3,1]],[[3,0],[3,1]],[[3,1],[4,0]],[[4,0],[5,0]],[[5,0],[6,0]]])
h('17.8 Evaluation Metrics')
table('Metric|Description|Use Case', 'Accuracy|Correctness of model output|Classification, QA', 'F1 Score|Balance of precision and recall|Information extraction', 'BLEU / ROUGE|Text-overlap similarity|Summarization tasks', 'Human Evaluation|Manual review of responses|General use case', 'Domain-Specific Metrics|Custom task metrics|Enterprise applications')
h('17.9 Key Takeaways')
li('Fine-tuning adapts a pre-trained model to tasks and domains.', 'LoRA and QLoRA are parameter-efficient techniques.', 'Use high-quality, domain-specific training data.', 'Evaluate with appropriate metrics.', 'Deploy with monitoring and continued evaluation.', 'Choose a method based on data, compute, cost and performance requirements.')
note('Fine-tuning does not guarantee fewer hallucinations or fresh facts. Measure against a baseline, protect sensitive training data and prevent train/test leakage. Instruction tuning describes the data/objective and can use full fine-tuning or PEFT; these categories overlap. Framework features in the source are examples, not version-specific installation instructions.')

b = page(19, 'Real-World Generative AI System Design', '1792805788985.jpeg')
h('18.1 What is Generative AI System Design?')
li('Designing end-to-end systems that use LLMs to solve real-world problems.', 'Includes data ingestion, storage, retrieval, inference, caching, monitoring and scaling.', 'Focuses on reliability, low latency, cost control and safety.', 'Used for chatbots, document Q&A, search, content generation and code assistants.')
h('18.2 Key Components')
table('Component|Description', 'Data Sources|Documents, PDFs, websites, databases, APIs', 'Ingestion Pipeline|Load, parse and chunk data', 'Embedding Model|Convert text into vectors', 'Vector Database|Store/search embeddings: Pinecone, Qdrant, Weaviate', 'LLM|Generate final answer using retrieved context', 'Orchestration Layer|Manage workflow: LangChain, LlamaIndex or custom code', 'API Layer|Expose functionality, e.g. FastAPI', 'Caching|Store repeated queries and responses, e.g. Redis', 'Monitoring|Track performance, logs and errors, e.g. ELK/Grafana')
h('18.3 High-Level Architecture')
flow('Application request and document-ingestion paths', ('User (Frontend)', 'Data Sources\nPDF, DB, Web'), ('API Gateway\nAuth, Rate Limit', 'Ingestion Pipeline\nLoad, Parse, Chunk'), ('Application Layer\nLangChain / Custom', 'Embedding Model\nOpenAI / SBERT'), ('LLM\nProvider / self-hosted', 'Vector DB\nEmbeddings', 'Cache\nRedis'), edges=[[[0,0],[1,0]],[[0,1],[1,1]],[[1,0],[2,0]],[[1,1],[2,1]],[[2,1],[3,1]],[[2,0],[3,1]],[[3,1],[2,0]],[[2,0],[3,0]],[[2,0],[3,2]],[[3,2],[2,0]]])
h('18.4 Detailed Workflow (RAG Example)')
flow('RAG request lifecycle', '1. User Query\nUser asks a question', '2. Query Processing\nClean, rephrase, create embedding', '3. Similarity Search\nFind relevant chunks in Vector DB', '4. Context Construction\nCombine retrieved chunks with prompt', '5. LLM Inference\nGenerate answer using context', '6. Post Processing\nFormat answer, add verified citations', '7. Response to User')
h('18.5 Design Considerations')
table('Aspect|Considerations', 'Latency|Caching, smaller models, optimized retrieval', 'Scalability|Load balancing, autoscaling, stateless services', 'Cost|Efficient models, caching, batch processing', 'Data Freshness|Update and re-index data', 'Security|Authentication, authorization and encryption', 'Reliability|Monitoring, logging, fallback models', 'Evaluation|Metrics to assess answer quality', 'User Experience|Fast response, streaming, citations, good UI/UX')
h('18.6 Example: Enterprise Document Q&A System')
flow('Enterprise document question answering', ('User (Web App)', 'Company Documents\nPDF, DOCX, Confluence, DB'), ('FastAPI\nAPI Layer', 'Loader & Chunking\nSplit, Clean'), ('LangChain\nOrchestration', 'Embedding Model\nOpenAI / SBERT'), ('LLM\nProvider / LLaMA', 'Vector DB\nQdrant / Pinecone', 'Cache\nRedis'), edges=[[[0,0],[1,0]],[[0,1],[1,1]],[[1,0],[2,0]],[[1,1],[2,1]],[[2,1],[3,1]],[[2,0],[3,1]],[[3,1],[2,0]],[[2,0],[3,0]],[[2,0],[3,2]],[[3,2],[2,0]]])
h('18.7 Real-World Use Cases')
table('Use Case|Description', 'Enterprise Chatbot|Answer questions from internal documents', 'Customer Support|Automate support with company knowledge base', 'Code Assistant|Generate/explain code using internal repositories', 'Document Summarization|Summarize reports, contracts and research papers', 'Healthcare Assistant|Answer queries using trusted medical documents', 'Legal Document Analysis|Extract key information from legal contracts', 'Education Assistant|Personalized learning using textbooks and notes', 'Business Analytics|Generate insights from internal data and reports')
h('18.8 Best Practices')
li('Use high-quality, domain-specific data.', 'Implement appropriate chunking and metadata.', 'Consider hybrid vector + keyword search.', 'Add verified citations for transparency.', 'Cache frequent queries with isolation and freshness rules.', 'Monitor performance and user feedback.', 'Implement safety checks and content filtering.', 'Continuously evaluate and improve.')
h('18.9 Common Challenges and Solutions')
table('Challenge|Possible Solution', 'Irrelevant Answers|Better chunking, hybrid search, reranking', 'High Latency|Caching, smaller models, optimized infrastructure', 'High Cost|Efficient models, less unnecessary context, caching', 'Outdated Information|Data updates and re-indexing', 'Hallucinations|RAG, citations, validation and guardrails', 'Data Security|Access control, encryption, appropriate private deployment', 'Scaling Issues|Load balancing, autoscaling; Kubernetes when justified', 'Evaluation Difficulty|Automated checks plus human review')
h('18.10 Key Takeaways')
li('System design matters when building production AI applications.', 'RAG is a common architecture for document-grounded answers.', 'Focus on scalability, cost, security and quality.', 'Choose tools and frameworks for the use case.', 'Continuously monitor, evaluate and improve.')
note('The diagrams are conceptual, not production deployment blueprints. Authenticate each request; enforce tenant/document authorization before retrieval and in tools; partition caches by authorization scope. Set deadlines, retry budgets, safe fallback behavior and deletion/re-indexing rules. High-stakes medical or legal outputs need appropriate expert validation. A retrieved citation must remain linked to the document version actually used.')

b = page(20, 'Generative AI Interview Questions and Final Revision', '1792805788949.jpeg')
h('19.1 Important Interview Topics')
li('LLM fundamentals: architecture, training, inference.', 'Prompt engineering and advanced techniques.', 'RAG: retrieval, embeddings, vector databases.', 'LangChain and LlamaIndex.', 'Fine-tuning: PEFT, LoRA, QLoRA, instruction tuning.', 'Evaluation metrics and hallucination control.', 'Model deployment and scaling.', 'Security, cost control and performance.', 'Real-world system design and use cases.')
h('19.2 LLM Fundamentals — Sample Questions')
table('No.|Question|Key Points to Cover', '1|What are LLMs?|Definition, pre-training, Transformer, use cases', '2|How does a Transformer work?|Attention, self-attention, encoder-decoder, tokens', '3|What is the difference between BERT and GPT?|Architecture, use cases, training objective', '4|What are token, context window and temperature?|Tokenization, context length, sampling and output variation', '5|What are hallucinations?|Causes, examples, mitigation techniques')
h('19.3 Prompt Engineering — Sample Questions')
table('No.|Question|Key Points to Cover', '1|What is prompt engineering?|Definition, importance, examples', '2|How do you write effective prompts?|Clear instructions, examples, format, constraints', '3|What are few-shot, zero-shot and chain-of-thought?|Differences, use cases, inspectable explanations', '4|What is prompt templating?|Dynamic prompts, variables', '5|What are guardrails in prompting?|Safety, checks, role-based prompts and their limits')
h('19.4 RAG and Vector Databases — Sample Questions')
table('No.|Question|Key Points to Cover', '1|What is RAG?|Definition, components, benefits', '2|How does semantic search work?|Embeddings, similarity, vector DB', '3|Which vector databases have you used?|Examples in source: Pinecone, Qdrant, Weaviate; describe your actual experience', '4|How do you chunk documents?|Chunk size, overlap, strategies', '5|How do you improve retrieval quality?|Better chunking, metadata, reranking, hybrid search')
h('19.5 Fine-Tuning and Adaptation — Sample Questions')
table('No.|Question|Key Points to Cover', '1|What is fine-tuning?|Full fine-tuning vs PEFT', '2|What are LoRA and QLoRA?|Low-rank adaptation, 4-bit base weights', '3|How do you use instruction tuning?|Instruction-response data, chatbot/assistant tasks', '4|Which frameworks have you used?|Hugging Face, PEFT, TRL; discuss actual experience', '5|What are the challenges in fine-tuning?|Data quality, overfitting, cost, evaluation')
h('19.6 LangChain and LlamaIndex — Sample Questions')
table('No.|Question|Key Points to Cover', '1|What is LangChain?|Chains/workflows, agents, tools, memory', '2|What are LangChain agents?|Types, tool use, examples', '3|What is LlamaIndex?|Data ingestion, indexing, retrieval', '4|LangChain vs LlamaIndex?|Differences and use cases', '5|How do you integrate a vector DB with LangChain/LlamaIndex?|Steps, code, use case')
h('19.7 Deployment and Scaling — Sample Questions')
table('No.|Question|Key Points to Cover', '1|How do you deploy an LLM application?|FastAPI, Docker, Kubernetes where needed', '2|How do you handle high traffic?|Load balancing, autoscaling', '3|What are scaling strategies?|Horizontal/vertical scaling, caching', '4|How do you reduce inference cost?|Smaller models, quantization, caching, batch processing', '5|What monitoring tools do you use?|Prometheus, Grafana, ELK; explain what you measure')
h('19.8 System Design — Sample Questions')
table('No.|Question|Key Points to Cover', '1|Design a RAG-based Q&A system.|Architecture, components, flow', '2|Design a chatbot for internal documents.|Data ingestion, indexing, security', '3|Design a multi-agent AI system.|Agents, orchestration, tools', '4|How do you handle large documents?|Chunking, hierarchical indexing', '5|How do you ensure security and privacy?|Encryption, access control, PII handling')
h('19.9 Common Scenario-Based Questions')
table('No.|Question|Key Points to Cover', '1|How do you handle irrelevant answers?|Reranking, better retrieval, guardrails', '2|How do you reduce hallucinations?|RAG, citations, validation', '3|How do you choose the right model?|Task, cost, performance', '4|How do you evaluate model quality?|Accuracy, faithfulness, task metrics, RAGAS', '5|How do you improve prompt results?|Clear instruction, examples, context, format')
h('19.10 Final Revision Checklist')
b.append({'type':'checklist','items':['Understand LLM architecture and key concepts.', 'Practice prompt engineering with different techniques.', 'Revise RAG, embeddings and vector databases.', 'Go through LangChain and LlamaIndex workflows.', 'Understand fine-tuning: PEFT, LoRA, QLoRA.', 'Revise evaluation metrics, RAGAS and hallucination control.', 'Practice system design for real-world use cases.', 'Be familiar with deployment, scaling and monitoring.', 'Understand security, cost control and performance.', 'Go through common interview questions and coding examples.', 'Prepare real-world projects and explain your experience clearly.']})
note('These are the sample interview prompts and answer cues present in the image, not full worked solutions. The separate Mock Interviews section contains the previously added solved interview questions. Explain only tools and projects you have actually used; use the other examples for practice.')

enrich(PAGES)

PALETTE = [('#dbeafe','#1d4ed8'),('#d1fae5','#047857'),('#fef3c7','#92400e'),('#ede9fe','#6d28d9'),('#ffe4e6','#be123c'),('#cffafe','#0e7490')]

def svg_diagram(block, ident):
    if block['type'] == 'diffusion': return diffusion_svg()
    if block['type'] == 'scatter':
        return '''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="460" viewBox="0 0 960 460" role="img" aria-labelledby="title desc">
<title id="title">Illustrative embedding space</title><desc id="desc">A conceptual three-dimensional space with King, Man, Woman and Queen. These are not measured vectors.</desc>
<rect width="960" height="460" rx="20" fill="#f8fafc"/>
<g stroke="#64748b" stroke-width="3"><path d="M240 320 L530 390 M240 320 L80 410 M240 320 L240 60"/></g>
<g font-family="system-ui,sans-serif" font-size="24" fill="#334155"><text x="540" y="405">x</text><text x="55" y="427">y</text><text x="230" y="45">z</text></g>
<g font-family="system-ui,sans-serif" font-size="25"><circle cx="170" cy="220" r="9" fill="#2563eb"/><text x="85" y="200" fill="#1d4ed8">King</text><circle cx="330" cy="150" r="9" fill="#059669"/><text x="350" y="145" fill="#047857">Man</text><circle cx="350" cy="255" r="9" fill="#7c3aed"/><text x="370" y="260" fill="#6d28d9">Woman</text><circle cx="280" cy="380" r="9" fill="#e11d48"/><text x="305" y="390" fill="#be123c">Queen</text></g>
<rect x="555" y="130" width="370" height="175" rx="16" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
<g font-family="system-ui,sans-serif" font-size="22" fill="#78350f"><text x="580" y="175">King − Man ≈ Queen − Woman</text><text x="580" y="220">Semantic relationships:</text><text x="580" y="255">conceptual illustration only</text></g></svg>'''
    layers = block['layers']
    heights = []
    for layer in layers:
        width=min(650,(880-18*(len(layer)-1))/len(layer))
        columns=max(12,int((width-24)/11))
        heights.append(max(90, max(sum(max(1,len(textwrap.wrap(line, columns))) for line in label.split('\n'))*25+32 for label in layer)))
    ys, current = [], 95
    for height in heights:
        ys.append(current); current += height + 54
    height = current + 10
    result = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape(block["title"])}</title>',f'<desc id="desc">{escape(" → ".join(" / ".join(layer) for layer in layers))}</desc>',f'<rect width="960" height="{height}" rx="20" fill="#f8fafc"/>', '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#64748b"/></marker></defs>']
    result.append(f'<text x="32" y="47" font-family="system-ui,sans-serif" font-size="23" font-weight="700" fill="#0f172a">{escape(block["title"])}</text>')
    positions={}
    for r, layer in enumerate(layers):
        gap=18; w=min(650,(880-gap*(len(layer)-1))/len(layer)); start=(960-(w*len(layer)+gap*(len(layer)-1)))/2
        for col,label in enumerate(layer): positions[(r,col)]=(start+col*(w+gap),ys[r],w,heights[r])
    edges=block.get('edges')
    if edges is None: edges=[[[r,c],[r+1,d]] for r in range(len(layers)-1) for c in range(len(layers[r])) for d in range(len(layers[r+1]))]
    for src,dst in edges:
        x,y,w,hh=positions[tuple(src)]; xx,yy,ww,hhh=positions[tuple(dst)]
        if src[0]==dst[0]:
            if x<xx: path=f'M{x+w} {y+hh/2} L{xx} {yy+hhh/2}'
            else: path=f'M{x} {y+hh/2+16} L{xx+ww} {yy+hhh/2+16}'
        elif dst[0]==src[0]+1:
            path=f'M{x+w/2} {y+hh} L{xx+ww/2} {yy}'
        else:
            # Side rails keep skip/feedback connections clear of intervening nodes.
            rail=26 if src[0]<dst[0] else 934
            path=f'M{x if rail==26 else x+w} {y+hh/2} H{rail} V{yy+hhh/2} H{xx if rail==26 else xx+ww}'
        result.append(f'<path d="{path}" fill="none" stroke="#64748b" stroke-width="2.5" marker-end="url(#arrow)"/>')
    for (r,c),(x,y,w,hh) in positions.items():
        fill,stroke=PALETTE[(r+c)%len(PALETTE)]
        result.append(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="13" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        lines=[line for raw in layers[r][c].split('\n') for line in (textwrap.wrap(raw,max(12,int((w-24)/11))) or [''])]
        top=y+(hh-len(lines)*25)/2+19
        for i,line in enumerate(lines): result.append(f'<text x="{x+w/2}" y="{top+i*25}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="19" fill="{stroke}">{escape(line)}</text>')
    return ''.join(result)+'</svg>'

def render_block(block, index, n):
    kind=block['type']
    if kind=='heading': return f'<h3>{escape(block["text"])}</h3>'
    if kind in ('paragraph','note'): return f'<{ "aside" if kind=="note" else "p"}'+(' class="clarification"' if kind=='note' else '')+'>'+('<strong>Clarification.</strong> ' if kind=='note' else '')+escape(block['text'])+f'</{"aside" if kind=="note" else "p"}>'
    if kind=='list': return '<ul>'+''.join('<li>'+escape(x)+'</li>' for x in block['items'])+'</ul>'
    if kind=='checklist': return '<ul class="revision-checklist">'+''.join(f'<li><label><input type="checkbox" data-check="revision-{i}"> {escape(x)}</label></li>' for i,x in enumerate(block['items']))+'</ul>'
    if kind=='code': return f'<pre tabindex="0" aria-label="{escape(block["language"])} example"><code>{escape(block["text"])}</code></pre>'
    if kind=='table':
        return '<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable comparison table"><table><thead><tr>'+''.join('<th scope="col">'+escape(x)+'</th>' for x in block['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+escape(x)+('</th>' if i==0 else '</td>') for i,x in enumerate(row))+'</tr>' for row in block['rows'])+'</tbody></table></div>'
    if kind=='references':
        return '<p class="further-reading">Further reading: '+', '.join(f'<a href="{escape(link["url"])}" target="_blank" rel="noopener">{escape(link["label"])}</a>' for link in block['links'])+'</p>'
    if kind in ('diagram','scatter','diffusion'):
        name=f"page-{n:02}-{block.get('assetId',index):02}.svg"; (OUT/'diagrams'/name).write_text(svg_diagram(block,name),encoding='utf-8')
        block['path']='docs/generative-ai/diagrams/'+name
        transcript=' → '.join(' / '.join(layer) for layer in block.get('layers',[])) or 'A conceptual 3D space: King, Man, Woman, Queen. King − Man ≈ Queen − Woman; illustrative, not measured vectors.'
        mobile=''
        if block.get('layers'):
            stages=''.join('<li>'+''.join(f'<div class="flow-card tone-{(r+c)%6}">{escape(label).replace(chr(10),"<br>")}</div>' for c,label in enumerate(layer))+'</li>' for r,layer in enumerate(block['layers']))
            mobile=f'<div class="mobile-diagram"><h4>{escape(block["title"])}</h4><ol>{stages}</ol><p>Grouped cards show parallel paths. Open the full chart to inspect branches and feedback connections.</p></div>'
        return f'<figure>{mobile}<a class="diagram-image" href="diagrams/{name}" target="_blank" rel="noopener"><img src="diagrams/{name}" alt="{escape(block["title"])}" loading="lazy"><span class="mobile-chart-link">Open full colorful chart ↗</span></a><figcaption>{escape(block["title"])} · Select to open full size.</figcaption><details class="diagram-transcript"><summary>Text version of this diagram</summary><p>{escape(transcript)}</p></details></figure>'
    raise ValueError(kind)

def main():
    (OUT/'diagrams').mkdir(parents=True,exist_ok=True)
    toc=''.join(f'<li><a href="#page-{x["page"]:02}"><span>{x["page"]:02}</span> {escape(x["title"])}</a></li>' for x in PAGES)
    articles=[]
    for item in PAGES:
        n=item['page']; blocks=''.join(render_block(block,i,n) for i,block in enumerate(item['blocks']))
        previous=f'<a href="#page-{n-1:02}">← Previous section</a>' if n>1 else '<a href="#contents">Contents</a>'
        following=f'<a href="#page-{n+1:02}">Next section →</a>' if n<20 else '<a href="#contents">Back to contents ↑</a>'
        articles.append(f'<article id="page-{n:02}" class="note-section" aria-labelledby="title-{n}"><h2 id="title-{n}">{escape(item["title"])}</h2><label class="section-read"><input type="checkbox" data-check="page-{n}"> Mark this section studied</label>{blocks}<nav class="section-navigation" aria-label="Section {n} navigation">{previous}{following}</nav></article>')
    html='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Twenty illustrated Generative AI study-note sections: LLMs, prompts, attention, training, agents, RAG, evaluation and system design."><title>Generative AI — Complete Developer Study Notes</title><link rel="stylesheet" href="../../css/ai-notes.css"><script src="../../js/ai-notes.js" defer></script></head><body><a class="skip-link" href="#notes">Skip to study notes</a><header class="notes-hero"><div class="shell"><a class="back-link" href="../../index.html">← Learning hub · AI Engineering</a><div class="eyebrow">AI LEARNING / ILLUSTRATED STUDY NOTES</div><h1>Generative AI<span>Complete Developer Study Notes</span></h1><p>A complete Generative AI tutorial in one place. Concepts, practical examples, colorful diagrams, comparison tables, formulas and interview preparation.</p><div class="hero-tags"><span>20 subsections</span><span>Selectable text</span><span>Colorful SVG charts</span><span>Print friendly</span></div><div class="notes-tools"><label>Find in these notes<input id="notes-search" type="search" placeholder="Try: LoRA, causal mask, RAG…"></label><button id="print-notes" type="button">Print / Save PDF</button><button id="show-all" type="button">Show all sections</button><a href="#contents">Browse contents ↓</a></div><p id="notes-status" role="status" aria-live="polite">20 sections · Progress is stored in this browser.</p><noscript><p>All notes and charts are available without JavaScript. Use your browser’s Find and Print commands.</p></noscript></div></header><div class="shell notes-layout"><aside class="contents" id="contents"><h2>On this page</h2><ol>'''+toc+'''</ol><p>Study progress is local to this browser. Original photographs remain on your device.</p></aside><main id="notes">'''+''.join(articles)+'''</main></div><footer class="shell notes-footer"><a href="../../index.html">Return to the learning hub</a><p>Recreated from the supplied study-note images. Illustrative values and model/tool examples are labeled; clarifications are separate from the source notes.</p></footer></body></html>'''
    expected={Path(block['path']).name for page in PAGES for block in page['blocks'] if block.get('path')}
    for asset in (OUT/'diagrams').glob('page-*.svg'):
        if asset.name not in expected: asset.unlink()
    (OUT/'index.html').write_text(html,encoding='utf-8')
    (ROOT/'data/ai-study-notes.json').write_text(json.dumps(PAGES,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    path=ROOT/'data/questions.json'; questions=json.loads(path.read_text(encoding='utf-8'))
    content=[]
    for topic in PAGES:
        content.append({'type':'chapter','text':topic['title']})
        for block in topic['blocks']:
            entry=dict(block)
            if block['type'] in ('diagram','scatter','diffusion'):
                entry['type']='image';entry['text']=block['title']
            elif block['type'] in ('list','checklist'):
                entry['text']=' '.join(block['items'])
            elif block['type']=='table':
                entry['text']=' '.join(block['headers']+[' '.join(row) for row in block['rows']])
            content.append(entry)
    item={'id':406,'category':'AI Engineering — Illustrated Generative AI Notes','question':'Generative AI — complete illustrated developer study notes (20 subsections)?','priority':'High','answer':'Generative AI learns patterns from data to generate text, images, audio, video and code. These notes explain the concepts, architecture, implementation techniques and evaluation through diagrams, tables, formulas and examples.','notesPath':'docs/generative-ai/index.html','detailStatus':'Expanded','contentBlocks':content}
    existing=next((q for q in questions if q['id']==406),None)
    if existing: assert existing.get('notesPath')==item['notesPath']; existing.clear(); existing.update(item)
    else: questions.append(item)
    path.write_text(json.dumps(questions,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Built one HTML page with {len(PAGES)} subsections and {sum(x["type"] in ("diagram","scatter","diffusion") for p in PAGES for x in p["blocks"])} colorful SVG diagrams.')

if __name__ == '__main__': main()
