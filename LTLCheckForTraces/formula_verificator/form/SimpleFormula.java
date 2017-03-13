package formula_verificator.form;


public class SimpleFormula implements Formula{

	private String LTLFormula;
	
	public SimpleFormula() {
		LTLFormula = null;
	}
	

	public SimpleFormula(String lTLFormula) {
		super();
		LTLFormula = lTLFormula;
	}



	public String getLTLFormula() {
		return LTLFormula;
	} 
	
	
}
