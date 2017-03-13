'''
the purpose of thisscript is to build gateway with
java src that checks the LTL formula compliance with given trace

Author: Anton Yeshchenko
'''


from py4j.java_gateway import JavaGateway
from shared_variables import getInt_fromUnicode


gateway = JavaGateway()                   # connect to the JVM
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1,number2)

verificator_app = gateway.entry_point        # get the AdditionApplication instance
print verificator_app.addition(number1,number2)
print verificator_app.mama(10)

# formula = "(  <>(\"tumor marker CA-19.9\") ) \\/ ( <> (\"ca-125 using meia\") )  "
#
#
# formula_help_desk1 = "( <>(\"6\") ) "
# formula_help_desk2 = "( <>(\"2\") /\  ( <>(\"6\") ) )"
# formula_help_desk3 = "( <>(\"7\") \\/  <> (\"9\") \\/  <> (\"3\") \\/  <> (\"4\") \\/  <> (\"5\") \\/  <> (\"1\") \\/  <> (\"2\") ) "
# formula_help_desk4 = "( <>(\"1\") ) "
#
# formula_help_desk_cut_2_absence = "( !( <> (( \"7\" /\ X ( <> ( \"7\" ))))) )"
# formula_help_desk_cut_2_non_succ1 = "[]((\"6\" -> ! ( <> ( \"5\" ))))"
# formula_help_desk_cut_2_non_succ2 = "[]((\"6\" -> ! ( <> ( \"1\" ))))"
# formula_help_desk_cut_2_non_succ3 = "[]((\"6\" -> ! ( <> ( \"7\" ))))"
# formula_help_desk_cut_2_exits = "<> ( \"6\" )"
# formula_help_desk_cut_2_non_chain_succ1 = "[]((\"6\" -> X(!(\"1\"))))"
# formula_help_desk_cut_2_non_chain_succ2 = "[]((\"6\" -> X(!(\"2\"))))"
# formula_help_desk_cut_2_non_chain_succ3 = "[]((\"6\" -> X(!(\"5\"))))"
# formula_help_desk_cut_2_non_chain_succ4 = "[]((\"6\" -> X(!(\"7\"))))"
# #######
# formula_help_desk_cut_2_exactly1 = "(<>(\"6\") /\ !(<>((\"6\" /\ X(<>(\"6\"))))))"
# formula_help_desk_cut_2_exclusive_choice1 = "((<>(\"6\") \/ (\"1\")) /\ !((<>(\"6\") /\ <> (\"1\"))))"
# formula_help_desk_cut_2_exclusive_choice2 = "((<>(\"6\") \/ (\"2\")) /\ !((<>(\"6\") /\ <> (\"2\"))))"
# formula_help_desk_cut_2_exclusive_choice3 = "((<>(\"6\") \/ (\"5\")) /\ !((<>(\"6\") /\ <> (\"5\"))))"
# formula_help_desk_cut_2_exclusive_choice4 = "((<>(\"6\") \/ (\"4\")) /\ !((<>(\"6\") /\ <> (\"4\"))))"
# formula_help_desk_cut_2_exclusive_choice5 = "((<>(\"6\") \/ (\"7\")) /\ !((<>(\"6\") /\ <> (\"7\"))))"
#
# formula_help_desk_cut_2_exclusive_choice6 = "((<>(\"6\") \/ (\"9\")) /\ !((<>(\"6\") /\ <> (\"9\"))))"
#
#
#
# formula_env_permit1 = "( <>(\"45\") \\/  <> (\"46\") ) "
#
# formula_env_permit_res = "[]((\"1\") -> <> (\"2\"))"
# formula_env_permit_precendence = "[]!(\"1\")   \/   (!(\"1\")  U  (\"2\"))"
# formula_env_permit_exclusive = " (<> A   \/  <>B)  /\  ! (<> A   /\  <>B)"
# formula_env_permit = "([]((\"118\") -> <> (\"126\"))) "
# formula_12 = "((\"6\") \\/  <> (\"5\") \\/  <> (\"4\") \\/  <> (\"5\") ) "
# formula_bpi11 = " (<> \"97\"   \/  <> \"3\")  /\  ! (<> \"97\"   /\  <>\"3\")"
# formula_bpi13 = " (<> \"1\"   \/  <> \"2\")  /\  ! (<> \"1\"   /\  <>\"2\")"
#
# #============= CHECKS HAPPEN HERE
#
# formula_used_helpdesk = formula_help_desk_cut_2_absence + " /\ " + \
#                formula_help_desk_cut_2_non_succ1 + " /\ " + \
#                formula_help_desk_cut_2_non_succ2 + " /\ " + \
#                formula_help_desk_cut_2_non_succ3 + " /\ " + \
#                formula_help_desk_cut_2_exits  + " /\ " +  \
#                formula_help_desk_cut_2_non_chain_succ1 + " /\ " +  \
#                formula_help_desk_cut_2_non_chain_succ2 + " /\ " +  \
#                formula_help_desk_cut_2_non_chain_succ3 + " /\ " +  \
#                formula_help_desk_cut_2_non_chain_succ1  + " /\ " +  \
#                formula_help_desk_cut_2_exactly1 + " /\ " +  \
#                formula_help_desk_cut_2_exclusive_choice1 + " /\ " + \
#                formula_help_desk_cut_2_exclusive_choice2  + " /\ " + \
#                formula_help_desk_cut_2_exclusive_choice3  + " /\ " + \
#                formula_help_desk_cut_2_exclusive_choice4  + " /\ " +  \
#                formula_help_desk_cut_2_exclusive_choice5  + " /\ " +  \
#                formula_help_desk_cut_2_exclusive_choice6
#
# formula_bpi11_not_chain_succ1 = "[]((\"32\" -> X(!(\"15\"))))"
# formula_bpi11_not_chain_succ2 = "[]((\"15\" -> X(!(\"1\"))))"
# formula_bpi11_not_chain_succ3 = "[]((\"1\" -> X(!(\"15\"))))"
#
# formula_bpi11_choice1 = "<>(\"15\") \/ <>(\"1\")"
# formula_bpi11_choice2 = "<>(\"15\") \/ <>(\"32\")"
#
# formula_used_bpi11 = formula_bpi11_not_chain_succ1 + " /\ " + \
#                      formula_bpi11_not_chain_succ2 + " /\ " + \
#                      formula_bpi11_not_chain_succ3 + " /\ " + \
#                      formula_bpi11_choice1 + " /\ " + formula_bpi11_choice2
#
# formula_bpi17_succ = "( []((\"11\" -> <>(\"17\"))) /\ (( (!(\"17\") U \"11\" )) \/ ([](!(\"17\")))) )"
#
# formula_bpi17_succ2 = "( []((\"12\" -> <>(\"10\"))) /\ (( (!(\"10\") U \"17\" )) \/ ([](!(\"10\")))) )"
# formula_bpi17_exist = "(<>(\"19\") /\ !(<>((\"19\" /\ X(<>(\"19\"))))))"
# formula_bpi17_absence = "( !( <> (( \"18\" /\ X ( <> ( \"18\" ))))) )"
# formula_bpi17_absence2 = "( !( <> (( \"11\" /\ X ( <> ( \"11\" ))))) )"
# formula_bpi17_succ1 = "( []((\"6\" -> <>(\"22\"))) /\ (( (!(\"22\") U \"6\" )) \/ ([](!(\"22\")))) )"
#
# formula_17 = formula_bpi17_succ2 + " /\ " + \
#              formula_bpi17_absence + " /\ " + formula_bpi17_succ1
#
# formula_bpi13_succ1 = "( []((\"1\" -> <>(\"9\"))) /\ (( (!(\"9\") U \"1\" )) \/ ([](!(\"9\")))) )"
#
#
# formula_bpi13_suffix_only = "( <>(\"5\") /\  ( <>(\"6\") ) )"
#
# formula_bpi13_declareInferred1_exclusive_choice =  " (<> \"1\"   \/  <> \"8\")  /\  ! (<> \"1\"   /\  <>\"8\")"
# #formula_bpi13_declareInferred2 =  "[]((\"5\" -> ! ( <> ( \"1\" ))))" #all are satisfied
#
#
# formula_bpi14 = "( <>(\"6\") /\  ( <>(\"12\") ) )"
#
#
# mar8BPI13_alternate_responce = "[]( ( \"10\" -> X(( !(\"10\") U \"3\" )))) " #from 10 to 3
# # from 1 to 10
# mar8BPI13_alternate_precendence = "( ( !( \"10\" ) U \"1\" ) ) /\ ( ( \"10\" -> X( ( !( \"10\" ) U \"1\" ) ) ) ) ) /\ ! (\"10\" )"
# mar8BPI13_existence = "<> ( \"4\" )"
# mar8BPI13_precendence = "( ! (\"9\" ) U \"1\" ) \/ ([](!(\"9\"))) /\ ! (\"9\" )" #from 1 to 9
# mar8BPI13_chain_precedence = "[]( ( X( \"5\"  ) -> \"3\" ) )/\ ! (\"5\"  )" #from 3 to 5
# mar8BPI13_choice = "( <> ( \"1\" ) \/ <>( \"3\" ) )"
# mar8BPI13_chain_responce = "[] ( ( \"12\" -> X( \"1\" ) ) )" #from 12 to 1
#
# formula_bpi13_mined_8_march_alpha_1_support_100_20_percent_of_testingtraces_all_formulas_declaleMiner = \
#     mar8BPI13_alternate_responce  + " /\ " + \
#     mar8BPI13_alternate_precendence   + " /\ " + \
#     mar8BPI13_existence   + " /\ " + \
#     mar8BPI13_precendence   + " /\ " + \
#     "[]( ( \"12\" -> X(( !(\"12\") U \"5\" )))) "  + " /\ " + \
#     mar8BPI13_chain_precedence  + " /\ " + \
#     "( ( !( \"5\" ) U \"1\" ) ) /\ ( ( \"5\" -> X( ( !( \"5\" ) U \"1\" ) ) ) ) ) /\ ! (\"5\" )" + " /\ " + \
#     mar8BPI13_choice + " /\ " + \
#     "[]( ( \"12\" -> X(( !(\"12\") U \"3\" )))) " + " /\ " + \
#     "[]( ( X( \"12\"  ) -> \"3\" ) )/\ ! (\"12\"  )" + " /\ " + \
#     mar8BPI13_chain_responce + " /\ " + \
#     "( ( !( \"12\" ) U \"1\" ) ) /\ ( ( \"12\" -> X( ( !( \"12\" ) U \"1\" ) ) ) ) ) /\ ! (\"12\" )"
#
# mar8BPI13_responce = "[]( ( \"1\" -> <>( \"6\" ) ) )"  #1 to 6
# formula_HELPDESK_mined_8_march_alpha_1_support_100_20_percent_of_testingtraces_all_formulas_declaleMiner = \
#     "[] ( ( \"3\" -> X( \"1\" ) ) )" + " /\ " + \
#     "[]( ( \"3\" -> X(( !(\"3\") U \"8\" )))) "+ " /\ " + \
#     "[]( ( \"3\" -> X(( !(\"3\") U \"6\" )))) "+ " /\ " + \
#     "( ( !( \"2\" ) U \"1\" ) ) /\ ( ( \"2\" -> X( ( !( \"2\" ) U \"1\" ) ) ) ) ) /\ ! (\"2\" )"+ " /\ " + \
#     "( <> ( \"1\" ) \/ <>( \"8\" ) )" + " /\ " + \
#     mar8BPI13_responce + " /\ " + \
#     "[] ( ( \"2\" -> X( \"6\" ) ) )"  + " /\ " + \
#     "[]( ( \"8\" -> <>( \"6\" ) ) )" + " /\ " + \
#     "[]( ( \"9\" -> <>( \"6\" ) ) )" + " /\ " + \
#     "( ( !( \"2\" ) U \"9\" ) ) /\ ( ( \"2\" -> X( ( !( \"2\" ) U \"9\" ) ) ) ) ) /\ ! (\"2\" )"  + " /\ " + \
#     "[]( ( X( \"2\"  ) -> \"8\" ) )/\ ! (\"2\"  )"
#
#
# BPI11_strong = "[]( ( \"7\" -> <>( \"15\" ) ) )  /\  []( ( \"0\" -> <>( \"1\" ) ) ) /\ <>\"0\" /\ <>\"7\" "
# BPI11_weak = "<>(\"0\") /\ <>(\"15\")"




def verify_formula_as_compliant(trace,formula,  prefix = 0):
    trace_new = gateway.jvm.java.util.ArrayList()
    for i in range(prefix, len(trace)):
        trace_new.append(str(getInt_fromUnicode(trace[i])))
    if not trace_new:
        return False
    ver = verificator_app.isTraceViolated(formula, trace_new) == False
 #   print str(ver)
    return ver


