public class Pattern267 {
 interface Button { String render(); }
 interface Checkbox { String render(); }
 // Factory Method: subclass supplies one product to a stable workflow.
 static abstract class Dialog {
  abstract Button createButton();
  String render(){return createButton().render();}
 }
 static class WebDialog extends Dialog {Button createButton(){return ()->"web button";}}
 // Abstract Factory: one family produces compatible related products.
 interface UiFactory {Button button();Checkbox checkbox();}
 static class DarkUi implements UiFactory {
  public Button button(){return ()->"dark button";}
  public Checkbox checkbox(){return ()->"dark checkbox";}
 }
 // Builder: assemble one complex value and validate at the boundary.
 record Report(String title,boolean includeChart) {
  static class Builder {
   private String title;private boolean chart;
   Builder title(String value){title=value;return this;}
   Builder includeChart(){chart=true;return this;}
   Report build(){if(title==null||title.isBlank())throw new IllegalStateException("title required");return new Report(title,chart);}
  }
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args){
  check(new WebDialog().render().equals("web button"));
  UiFactory factory=new DarkUi();
  check(factory.button().render().startsWith("dark")&&factory.checkbox().render().startsWith("dark"));
  Report report=new Report.Builder().title("Audit").includeChart().build();check(report.includeChart());
  try{new Report.Builder().build();throw new AssertionError();}catch(IllegalStateException expected){}
  System.out.println("PASS: factory workflow, related family and builder validation");
 }
}
