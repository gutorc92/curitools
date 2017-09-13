import unittest
import curitools.requestpages.pages as rp
import os

class TestSubPage(unittest.TestCase):


    def test_gettext(self):
        repositorio_dir = os.path.dirname(os.path.realpath(__file__))
        file_submit = os.path.join(repositorio_dir, "1011.cpp")
        sub = rp.SubmissionPage(session=None,problem="1011", file_path=file_submit)
        text = """
            #include<iostream>                                                              
            
            using namespace std;                                                            
                                                                                   
            int main(){                                                                     
                 int total = 10;                                                             
                 cout << "VALOR A PAGAR: R$ " << total <<endl;                               
                 return 1 ;                                                                  
             }
        """
        assert sub.read_file() == text
 
    def test_submission(self):
        try:
            login = rp.LoginPage()
            login.run()
        except HTTPError:
            sys.exit()
    
        repositorio_dir = os.path.dirname(os.path.realpath(__file__))
        file_submit = os.path.join(repositorio_dir, "1010.cpp")
        sub = rp.SubmissionPage(login.get_session(),"1010", file_submit)
        assert sub.run() == True
    
if __name__ == '__main__':
    unittest.main()
