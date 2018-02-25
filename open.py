import webbrowser
n = 5854 
data = "http://www.amazon.co.uk/gp/pdp/profile/A35BGQOWVHREX4/ref=cm_cr_tr_tbl_"
url = data +str(n)+"_name"
webbrowser.open_new_tab(url)
               
for n in range (n,5860):
    url = data +str(n)+"_name"
    webbrowser.open_new_tab(url)
    n = n+1
               
