# Based on testing harness dated 2021-03-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
#   
#   MAC:
#   python3 <thisfile.py> <your_one_file.py>
# 
#   PC:
#   python <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2
# 
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
# 
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.
#  Edited by Ana Loreto, March 2021.

import unittest
import shutil
import sys
import os
import time

#import subprocess

import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
    
REQUIRED_DEFNS = [  "dif_fibcumsum",
                    "dif_oddsumcount",
                    "is_promotion",
                    "biggest_sale",
                    "marble_cakes",
                    "get_cakewithtopping",
                    "sales_sort",
                    "dif_sales",
                 ]

# for method names in classes that will be tested. They have to be here
# so that we don't complain about missing global function definitions.
# Really, any chosen name for test batches can go here regardless of actual
# method names in the code.
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = [ ]

# how many points are test cases worth?
weight_required     = 1
weight_extra_credit = 1

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 80

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode... 
CURRENTLY_GRADING = False


# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"


import inspect # for enforcing usage of an operator or function
import ast     # for enforcing usage of an operator or function

# checks if a call to the function is present in the code. Of course it 
# might not actually be used in their solution...
def enforce_func_usage(func, funcname):
    dumptext = ast.dump(ast.parse(inspect.getsource(func).strip()))
    batches = dumptext.split("value=Call")
    for batch in batches:
        parts = batch.split("attr=")
        for part in parts:
            if part.startswith("'"+funcname+"'"):
                return
    raise Exception("You're required to call "+funcname+" in your solution.")


# END SPECIALIZATION SECTION

################################################################################
################################################################################
################################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
        
    ############################################################################
    
    def test_dif_fibcumsum_1(self): self.assertEqual(dif_fibcumsum(5),10)
    def test_dif_fibcumsum_2(self): self.assertEqual(dif_fibcumsum(1),0)
    def test_dif_fibcumsum_3(self): self.assertEqual(dif_fibcumsum(3),4)
    def test_dif_fibcumsum_4(self): self.assertEqual(dif_fibcumsum(8),15)
    def test_dif_fibcumsum_5(self): self.assertEqual(dif_fibcumsum(4),7)
    def test_dif_fibcumsum_6(self): self.assertEqual(dif_fibcumsum(100),354224848179261910025)
    def test_dif_fibcumsum_7(self): self.assertEqual(dif_fibcumsum(50),12586267750)
    def test_dif_fibcumsum_8(self): self.assertEqual(dif_fibcumsum(25),74700)
    def test_dif_fibcumsum_9(self): self.assertEqual(dif_fibcumsum(99),218922995834555164076)
    def test_dif_fibcumsum_10(self): self.assertEqual(dif_fibcumsum(2),2)

    ########################################################################### 
    
    def test_dif_oddsumcount_1(self): self.assertEqual(dif_oddsumcount(5),6)
    def test_dif_oddsumcount_2(self): self.assertEqual(dif_oddsumcount(1),0)
    def test_dif_oddsumcount_3(self): self.assertEqual(dif_oddsumcount(3),2)
    def test_dif_oddsumcount_4(self): self.assertEqual(dif_oddsumcount(15),56)
    def test_dif_oddsumcount_5(self): self.assertEqual(dif_oddsumcount(4),2)
    def test_dif_oddsumcount_6(self): self.assertEqual(dif_oddsumcount(100),2450)
    def test_dif_oddsumcount_7(self): self.assertEqual(dif_oddsumcount(49),600)
    def test_dif_oddsumcount_8(self): self.assertEqual(dif_oddsumcount(26),156)
    def test_dif_oddsumcount_9(self): self.assertEqual(dif_oddsumcount(99),2450)
    def test_dif_oddsumcount_10(self): self.assertEqual(dif_oddsumcount(2),0)
 
    ########################################################################### 
    
    def test_is_promotion_1(self): self.assertEqual(is_promotion("carrot", ["chocolate","almond","carrot"]),True)
    def test_is_promotion_2(self): self.assertEqual(is_promotion("carrot", ["ch-ca", "lemon","velvet"]),False)
    def test_is_promotion_3(self): self.assertEqual(is_promotion("carrot",[]),False)
    def test_is_promotion_4(self): self.assertEqual(is_promotion("ch-va",["velvet","va"]),False)
    def test_is_promotion_5(self): self.assertEqual(is_promotion("banana",["almond","carrot"]),False)
    def test_is_promotion_6(self): self.assertEqual(is_promotion("ba-ca",[]),False)
    def test_is_promotion_7(self): self.assertEqual(is_promotion("almond",["almond","carrot"]),True)
    def test_is_promotion_8(self): self.assertEqual(is_promotion("lemon",["velvet","pistachio","carrot"]),False)
    def test_is_promotion_9(self): self.assertEqual(is_promotion("pistachio",["pistachio"]),True)
    def test_is_promotion_10(self): self.assertEqual(is_promotion("pi-le",["pineapple","va-le"]),False)
   
    ########################################################################### 
    
    def test_biggest_sale_1(self): self.assertEqual(biggest_sale(["vanilla","ch-ca"], [4,15], ["vanilla","almond"]), "marble")
    def test_biggest_sale_2(self): self.assertEqual(biggest_sale(["chocolate"], [], ["chocolate","carrot","vanilla"]), None)
    def test_biggest_sale_3(self): self.assertEqual(biggest_sale([],[],["lemon"]),None)
    def test_biggest_sale_4(self): self.assertEqual(biggest_sale(["almond","banana","ch-ba"],[5,9,6],["banana","carrot","vanilla","almond"]), "single")
    def test_biggest_sale_5(self): self.assertEqual(biggest_sale(["al-va"],[1],[]), "marble")
    def test_biggest_sale_6(self): self.assertEqual(biggest_sale(["almond","banana",'ch-al'],[5,5,5],[]), "marble")
    def test_biggest_sale_7(self): self.assertEqual(biggest_sale(["almond","banana","carrot"],[3,4,5],["chocolate"]),"marble")
    def test_biggest_sale_8(self): self.assertEqual(biggest_sale(["ba-ca","ch-al","pi-ca"],[150,5,13], ["ba-ca"]),"single")
    def test_biggest_sale_9(self): self.assertEqual(biggest_sale(["a","b","c"],[3,4,5],["x","y","a"]),"marble")
    def test_biggest_sale_10(self): self.assertEqual(biggest_sale(["almond"],[150], ["chocolate","almond"]),"single")

    ########################################################################### 
    
    def test_marble_cakes_1(self): self.assertEqual(marble_cakes("chocolate", ["vanilla","almond"]),3)
    def test_marble_cakes_2(self): self.assertEqual(marble_cakes("chocolate", ["chocolate"]),0)
    def test_marble_cakes_3(self): self.assertEqual(marble_cakes("chocolate", ["carrot","chocolate"]),1)
    def test_marble_cakes_4(self): self.assertEqual(marble_cakes("almond",["vanilla","almond","velvet","banana","oreo"]),10)
    def test_marble_cakes_5(self): self.assertEqual(marble_cakes("carrot",["chocolate","oreo","vanilla"]),6)
    def test_marble_cakes_6(self): self.assertEqual(marble_cakes("lemon",["lemon","banana","vanilla"]),3)
    def test_marble_cakes_7(self): self.assertEqual(marble_cakes("almond",["banana","carrot","vanilla","almond"]),6)
    def test_marble_cakes_8(self): self.assertEqual(marble_cakes("al-va",[]),0)
    def test_marble_cakes_9(self): self.assertEqual(marble_cakes("almond",["banana","oreo","pineapple","white","velvet"]),15)
    def test_marble_cakes_10(self): self.assertEqual(marble_cakes("pineapple",["pistachio","almond","banana","carrot","vanilla","chocolate"]),21)  

    ########################################################################### 

    def test_get_cakewithtopping_1(self): self.assertEqual(get_cakewithtopping("carrot",["MM","oreo"]),['carrot-MM', 'carrot-oreo'])
    def test_get_cakewithtopping_2(self): self.assertEqual(get_cakewithtopping("pistachio",["sprinkles"]),['pistachio-sprinkles'])
    def test_get_cakewithtopping_3(self): self.assertEqual(get_cakewithtopping("velvet",[]),[])
    def test_get_cakewithtopping_4(self): self.assertEqual(get_cakewithtopping("almond",["MM","chocochisp","-","suggarcream","oreo"]),['almond-MM', 'almond-chocochisp', 'almond--', 'almond-suggarcream', 'almond-oreo'])
    def test_get_cakewithtopping_5(self): self.assertEqual(get_cakewithtopping("ca-va",["chocochisp","oreo","MM"]),['ca-va-chocochisp', 'ca-va-oreo', 'ca-va-MM'])
    def test_get_cakewithtopping_6(self): self.assertEqual(get_cakewithtopping("ch-ve",["-","Milky-Way","MM"]),['ch-ve--', 'ch-ve-Milky-Way', 'ch-ve-MM'])
    def test_get_cakewithtopping_7(self): self.assertEqual(get_cakewithtopping("banana",["oreo","carrot","MM","cookies"]),['banana-oreo', 'banana-carrot', 'banana-MM', 'banana-cookies'])
    def test_get_cakewithtopping_8(self): self.assertEqual(get_cakewithtopping("al-va",["Milky-Way"]),['al-va-Milky-Way'])
    def test_get_cakewithtopping_9(self): self.assertEqual(get_cakewithtopping("almond",["cookies","oreo","sprinkles","kisses","-"]),['almond-cookies', 'almond-oreo', 'almond-sprinkles', 'almond-kisses', 'almond--'])
    def test_get_cakewithtopping_10(self): self.assertEqual(get_cakewithtopping("pinepple",["pistachios","almonds","sprinkles","suggarcream","cheesecake","peanuts"]),['pinepple-pistachios', 'pinepple-almonds', 'pinepple-sprinkles', 'pinepple-suggarcream', 'pinepple-cheesecake', 'pinepple-peanuts'])
    
    ########################################################################### 
    
    def test_sales_sort_1(self): self.assertEqual(sales_sort(["pistachio","velvet"],[8,7]),['pistachio', 'velvet'])
    def test_sales_sort_2(self): self.assertEqual(sales_sort([],[]),[])
    def test_sales_sort_3(self): self.assertEqual(sales_sort(["lemon","carrot","dark"],[2,50,50]),['carrot', 'dark', 'lemon'])
    def test_sales_sort_4(self): self.assertEqual(sales_sort(["vanilla","ch-ca"],[4,15]),['ch-ca', 'vanilla'])
    def test_sales_sort_5(self): self.assertEqual(sales_sort(["chocolate","carrot","vanilla"],[500,1,1]),['chocolate', 'carrot', 'vanilla'])
    def test_sales_sort_6(self): self.assertEqual(sales_sort(["lemon"],[0]),['lemon'])
    def test_sales_sort_7(self): self.assertEqual(sales_sort(["ba-ca","ch-al","pi-ca"],[150,5,13]),['ba-ca', 'pi-ca', 'ch-al'])
    def test_sales_sort_8(self): self.assertEqual(sales_sort(["va-le","al-va"],[1,1]),['va-le', 'al-va'])
    def test_sales_sort_9(self): self.assertEqual(sales_sort(["almond","banana",'ch-al'],[5,5,5]),['almond', 'banana', 'ch-al'])
    def test_sales_sort_10(self): self.assertEqual(sales_sort(["almond","banana","ch-ba"],[0,6,9],),['ch-ba', 'banana', 'almond'])
    
    ###########################################################################

    def test_dif_sales_1(self): self.assertEqual(dif_sales(["carrot","velvet","lemon"], [1,5,1]),['velvet'])
    def test_dif_sales_2(self): self.assertEqual(dif_sales(["chocolate","vanilla"], [9,1]),['chocolate', 'vanilla'])
    def test_dif_sales_3(self): self.assertEqual(dif_sales(["velvet","white","dark","banana"], [2,5,5,2]),[])
    def test_dif_sales_4(self): self.assertEqual(dif_sales(["carrot","velvet","vanilla","ch-ca","chocolate","lemon"],[100,10,15,0,0,100]),['velvet', 'vanilla'])
    def test_dif_sales_5(self): self.assertEqual(dif_sales(["almond","banana",'ch-al'],[5,5,5]),[])
    def test_dif_sales_6(self): self.assertEqual(dif_sales([],[]),[])
    def test_dif_sales_7(self): self.assertEqual(dif_sales(["lemon","carrot","dark"],[2,50,50]),['lemon'])
    def test_dif_sales_8(self): self.assertEqual(dif_sales(["velvet","ch-ca","chocolate","carrot","vanilla","lemon"],[0,15,1,0,1,6]),['ch-ca', 'lemon'])
    def test_dif_sales_9(self): self.assertEqual(dif_sales(["va-le","al-va","ca-pi"],[500,1,1]),['va-le'])
    def test_dif_sales_10(self): self.assertEqual(dif_sales(["white"],[0]),['white'])
    
    ########################################################################### 

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
    # constructor.
    def __init__(self,wants):
        self.num_req = 0
        self.num_ec = 0
        # find all methods that begin with "test".
        fs = []
        for w in wants:
            for func in AllTests.__dict__:
                # append regular tests
                # drop any digits from the end of str(func).
                dropnum = str(func)
                while dropnum[-1] in "1234567890":
                    dropnum = dropnum[:-1]
                
                if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
                    fs.append(AllTests(str(func)))
                if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
                    fs.append(AllTests(str(func)))
        
#       print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
        # call parent class's constructor.
        unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
        # constructor.
        def __init__(self,wants):
            # find all methods that begin with "test_extra_credit_".
            fs = []
            for w in wants:
                for func in AllTests.__dict__:
                    if str(func).startswith("test_extra_credit_"+w):
                        fs.append(AllTests(str(func)))
        
#           print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
            # call parent class's constructor.
            unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
    this_file = __file__
    if dir==".":
        dir = os.getcwd()
    info = os.walk(dir)
    filenames = []
    for (dirpath,dirnames,filez) in info:
#       print(dirpath,dirnames,filez)
        if dirpath==".":
            continue
        for file in filez:
            if file==this_file:
                continue
            filenames.append(os.path.join(dirpath,file))
#       print(dirpath,dirnames,filez,"\n")
    return filenames

def main():
    if len(sys.argv)<2:
        raise Exception("needed student's file name as command-line argument:"\
            +"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")
    
    if BATCH_MODE:
        print("BATCH MODE.\n")
        run_all()
        return
        
    else:
        want_all = len(sys.argv) <=2
        wants = []
        # remove batch_mode signifiers from want-candidates.
        want_candidates = sys.argv[2:]
        for i in range(len(want_candidates)-1,-1,-1):
            if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
                del want_candidates[i]
    
        # set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
        wants = []
        extra_credits = []
        if not want_all:
            for w in want_candidates:
                if w in REQUIRED_DEFNS:
                    wants.append(w)
                elif w in SUB_DEFNS:
                    wants.append(w)
                elif w in EXTRA_CREDIT_DEFNS:
                    extra_credits.append(w)
                else:
                    raise Exception("asked to limit testing to unknown function '%s'."%w)
        else:
            wants = REQUIRED_DEFNS + SUB_DEFNS
            extra_credits = EXTRA_CREDIT_DEFNS
        
        # now that we have parsed the function names to test, run this one file.    
        run_one(wants,extra_credits)    
        return
    return # should be unreachable! 

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):
    
    has_reqs = len(wants)>0
    has_ec   = len(extra_credits)>0
    
    # make sure they exist.
    passed1 = 0
    passed2 = 0
    tried1 = 0
    tried2 = 0
    
    # only run tests if needed.
    if has_reqs:
        print("\nRunning required definitions:")
        (tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
    if has_ec:
        print("\nRunning extra credit definitions:")
        (tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
    
    # print output based on what we ran.
    if has_reqs and not has_ec:
        print("\n%d/%d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
        print("\nScore based on test cases: %.2f/%d (%.2f*%d) " % (
                                                                passed1*weight_required, 
                                                                total_points_from_tests,
                                                                passed1,
                                                                weight_required
                                                             ))
    elif has_ec and not has_reqs:
        print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
    else: # has both, we assume.
        print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
        print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
        print("\nScore based on test cases: %.2f / %d ( %d * %.2f + %d * %.2f) " % (
                                                                passed1*weight_required+passed2*weight_extra_credit, 
                                                                total_points_from_tests,
                                                                passed1,
                                                                weight_required,
                                                                passed2,
                                                                weight_extra_credit
                                                             ))
    if CURRENTLY_GRADING:
        print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
        filenames = files_list(sys.argv[1])
        #print(filenames)
        
        wants = REQUIRED_DEFNS + SUB_DEFNS
        extra_credits = EXTRA_CREDIT_DEFNS
        
        results = []
        for filename in filenames:
            print(" Batching on : " +filename)
            # I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
            lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()
            
            # delay of shame...
            time.sleep(DELAY_OF_SHAME)
            
            name = os.path.basename(lines[-1])
            stuff =lines[-2].split(" ")[1:-1]
            print("STUFF: ",stuff, "LINES: ", lines)
            (passed_req, tried_req, passed_ec, tried_ec) = stuff
            results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
            continue
        
        print("\n\n\nGRAND RESULTS:\n")
        
            
        for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
            name = os.path.basename(tag_req).strip()
            earned   = passed_req*weight_required + passed_ec*weight_extra_credit
            possible = tried_req *weight_required # + tried_ec *weight_extra_credit
            print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
                                                            name,
                                                            earned,
                                                            possible, 
                                                            (earned/possible)*100,
                                                            passed_req,tried_req,weight_required,
                                                            passed_ec,tried_ec,weight_extra_credit
                                                          ))
# only used for batch mode.
def run_all_orig():
        filenames = files_list(sys.argv[1])
        #print(filenames)
        
        wants = REQUIRED_DEFNS + SUB_DEFNS
        extra_credits = EXTRA_CREDIT_DEFNS
        
        results = []
        for filename in filenames:
            # wipe out all definitions between users.
            for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
                globals()[fn] = decoy(fn)
                fn = decoy(fn)
            try:
                name = os.path.basename(filename)
                print("\n\n\nRUNNING: "+name)
                (tag_req, passed_req, tried_req) = run_file(filename,wants,False)
                (tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
                results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
                print(" ###### ", results)
            except SyntaxError as e:
                tag = filename+"_SYNTAX_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except NameError as e:
                tag =filename+"_Name_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except ValueError as e:
                tag = filename+"_VALUE_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except TypeError as e:
                tag = filename+"_TYPE_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except ImportError as e:
                tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except Exception as e:
                tag = filename+str(e.__reduce__()[0])
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
        
#           try:
#               print("\n |||||||||| scrupe: "+str(scruples))
#           except Exception as e:
#               print("NO SCRUPE.",e)
#           scruples = None
        
        print("\n\n\nGRAND RESULTS:\n")
        for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
            name = os.path.basename(tag_req)
            earned   = passed_req*weight_required + passed_ec*weight_extra_credit
            possible = tried_req *weight_required # + tried_ec *weight_extra_credit
            print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
                                                            name,
                                                            earned,
                                                            possible, 
                                                            (earned/possible)*100,
                                                            passed_req,tried_req,weight_required,
                                                            passed_ec,tried_ec,weight_extra_credit
                                                          ))

def try_copy(filename1, filename2, numTries):
    have_copy = False
    i = 0
    while (not have_copy) and (i < numTries):
        try:
            # move the student's code to a valid file.
            shutil.copy(filename1,filename2)
            
            # wait for file I/O to catch up...
            if(not wait_for_access(filename2, numTries)):
                return False
                
            have_copy = True
        except PermissionError:
            print("Trying to copy "+filename1+", may be locked...")
            i += 1
            time.sleep(1)
        except BaseException as e:
            print("\n\n\n\n\n\ntry-copy saw: "+e)
    
    if(i == numTries):
        return False
    return True

def try_remove(filename, numTries):
    removed = False
    i = 0
    while os.path.exists(filename) and (not removed) and (i < numTries):
        try:
            os.remove(filename)
            removed = True
        except OSError:
            print("Trying to remove "+filename+", may be locked...")
            i += 1
            time.sleep(1)
    if(i == numTries):
        return False
    return True

def wait_for_access(filename, numTries):
    i = 0
    while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
        print("Waiting for access to "+filename+", may be locked...")
        time.sleep(1)
        i += 1
    if(i == numTries):
        return False
    return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
    if wants==None:
        wants = []
    
    # move the student's code to a valid file.
    if(not try_copy(filename,"student.py", 5)):
        print("Failed to copy " + filename + " to student.py.")
        quit()
        
    # import student's code, and *only* copy over the expected functions
    # for later use.
    import importlib
    count = 0
    while True:
        try:
#           print("\n\n\nbegin attempt:")
            while True:
                try:
                    f = open("student.py","a")
                    f.close()
                    break
                except:
                    pass
#           print ("\n\nSUCCESS!")
                
            import student
            importlib.reload(student)
            break
        except ImportError as e:
            print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
            time.sleep(0.5)
            while not os.path.exists("student.py"):
                time.sleep(0.5)
            count+=1
            if count>3:
                raise ImportError("too many attempts at importing!")
        except SyntaxError as e:
            print("SyntaxError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_SYNTAX_ERROR",None, None, None)
        except NameError as e:
            print("NameError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return((filename+"_Name_ERROR",0,1))    
        except ValueError as e:
            print("ValueError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_VALUE_ERROR",0,1)
        except TypeError as e:
            print("TypeError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_TYPE_ERROR",0,1)
        except ImportError as e:            
            print("ImportError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details or try again")
            return((filename+"_IMPORT_ERROR_TRY_AGAIN   ",0,1)) 
        except Exception as e:
            print("Exception in loading"+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+str(e.__reduce__()[0]),0,1)
    
    # make a global for each expected definition.
    for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
        globals()[fn] = decoy(fn)
        try:
            globals()[fn] = getattr(student,fn)
        except:
            if fn in wants:
                print("\nNO DEFINITION FOR '%s'." % fn) 
    
    if not checking_ec:
        # create an object that can run tests.
        runner = unittest.TextTestRunner()
    
        # define the suite of tests that should be run.
        suite = TheTestSuite(wants)
    
    
        # let the runner run the suite of tests.
        ans = runner.run(suite)
        num_errors   = len(ans.__dict__['errors'])
        num_failures = len(ans.__dict__['failures'])
        num_tests    = ans.__dict__['testsRun']
        num_passed   = num_tests - num_errors - num_failures
        # print(ans)
    
    else:
        # do the same for the extra credit.
        runner = unittest.TextTestRunner()
        suite = TheExtraCreditTestSuite(wants)
        ans = runner.run(suite)
        num_errors   = len(ans.__dict__['errors'])
        num_failures = len(ans.__dict__['failures'])
        num_tests    = ans.__dict__['testsRun']
        num_passed   = num_tests - num_errors - num_failures
        #print(ans)
    
    # remove our temporary file.
    os.remove("student.py")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    if(not try_remove("student.py", 5)):
        print("Failed to remove " + filename + " to student.py.")
    
    tag = ".".join(filename.split(".")[:-1])
    
    
    return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
        # this can accept any kind/amount of args, and will print a helpful message.
        def failyfail(*args, **kwargs):
            return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
        return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
    main()
