# '''
# the purpose of thisscript is to build gateway with
# java src that checks the LTL formula compliance with given trace
#
# Author: Anton Yeshchenko
# '''
#
# from py4j.java_gateway import JavaGateway
#
#
# gateway = JavaGateway()
# #
# # java_list = gateway.jvm.java.util.ArrayList()
# # java_list.append(214)
# # java_list.append(120)
# # gateway.jvm.java.util.Collections.sort(java_list)
# # print java_list
#
# stackEntryPoint = gateway.entry_point.a
#
# print stackEntryPoint
#
#

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1,number2)

verificator_app = gateway.entry_point        # get the AdditionApplication instance
print verificator_app.addition(number1,number2)
print verificator_app.mama(10)

formula = "(  <>(\"tumor marker CA-19.9\") ) \\/ ( <> (\"ca-125 using meia\") )  "

def verify_formula(trace):
    return verificator_app.isTraceViolated(formula,trace)


#print verify_formula("aaa")