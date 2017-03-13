//import formula_verificator.FormulaVerificator;
//import formula_verificator.XLogReader;
//import formula_verificator.form.Formula;
//import formula_verificator.form.SimpleFormula;
//import org.deckfour.xes.model.XLog;
//import org.deckfour.xes.model.XTrace;
//
//public class StackEntryPoint {
//
//    public static void main(String[] args) {
//        // Prints "Hello, World" to the terminal window.
//        System.out.println("Hello, World");
//
//        String[] phi = new String[]{
//                "(  <>(\"tumor marker CA-19.9\") ) \\/ ( <> (\"ca-125 using meia\") )  ",
//                "([](    ((\"CEA - tumor marker using meia\") -> ( <>(\"squamous cell carcinoma using eia\")))))",
//                "(  (! (\"histological examination - biopsies nno\")) U (\"squamous cell carcinoma using eia\"))",
//                "   ( <> (\"histological examination - big resectiep\") )   ",
//                "(<> (\"01_HOOFD_010\") ) /\\ ( <> (\"01_HOOFD_193\") )",
//                "( <>(\"08_AWB45_030\") ) \\/ ( <> (\"01_HOOFD_493\") )",
//                "[]( ( (\"01_HOOFD_020\") -> ( <>(\"08_AWB45_020_1\")) ) )"};
//
//
//        try {
//            XLog log = XLogReader.openLog("BPI2011_20.xes");
//            XTrace trace = log.get(0);
//
//            System.out.println("The result: " + FormulaVerificator.isTraceViolated(new SimpleFormula(phi[0]), trace));
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//
//
//
//    }
//
//    boolean isTraceViolated(Formula formula, XTrace trace){
//        return FormulaVerificator.isTraceViolated(formula,trace);
//    }
//}

//import formula_verificator.FormulaVerificator;
//import formula_verificator.form.Formula;
//import org.deckfour.xes.model.XTrace;
//import py4j.GatewayServer;
//
//public class StackEntryPoint {
//
//    private FormulaVerificator formulaVerificator;
//
//    public StackEntryPoint() {
//        formulaVerificator= new FormulaVerificator();
//    }
//
//    boolean isTraceViolated(Formula formula, XTrace trace){
//        return FormulaVerificator.isTraceViolated(formula,trace);
//    }
//
//    public String mama(){
//        return "Ciao! it works!";
//    }
//    public static String a =  "str!!lsfenfowejrqpfjwsdklvnsfkjrwe";
//
//    public static void main(String[] args) {
//        GatewayServer gatewayServer = new GatewayServer(new StackEntryPoint());
//        gatewayServer.start();
//        System.out.println("Gateway Server Started");
//    }
//
//}
//import formula_verificator.form.Formula;
//import org.deckfour.xes.model.XTrace;

import formula_verificator.FormulaVerificator;
import py4j.GatewayServer;
import java.util.ArrayList;

public class StackEntryPoint {




    public int addition(int first, int second) {
        return first + second;
    }

    public int mama(int l){
        return 10 + l;
    }

    public boolean isTraceViolated(String formula, ArrayList<String> trace){
        return FormulaVerificator.isTraceViolated(formula,trace);
    }

    public static void main(String[] args) {
        System.out.println("Gateway Server not yet Started");
        StackEntryPoint app = new StackEntryPoint();
        // app is now the gateway.entry_point
        GatewayServer server = new GatewayServer(app);
        server.start();
        System.out.println("Gateway Server Started");
    }
}