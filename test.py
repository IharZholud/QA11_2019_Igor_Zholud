Ну, удачи.

 chrome.find_element_by_xpath("//a[@class='et_pb_button et_pb_button_5 et_pb_bg_layout_light']").click()   
#клик кнопки в Section of Buttons

 chrome.find_element_by_xpath("//div[@class='et_pb_column et_pb_column_1_2 et_pb_column_7    et_pb_css_mix_blend_mode_passthrough']//a[@class='icon et_pb_with_border']").click()                                                                       
#клик Section of Social Media Follows

input1=chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_0 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//input[@type='text']")
input1.send_keys("Igor")
chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_0 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//input[@id='searchsubmit']").click()
#right Search

chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_0 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//img[@class='widgets-list-layout-blavatar']").click()
 #left icon

chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_0 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//a[@class='bump-view']").click()
 #left link

 email1=chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_0 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//input[@type='email']")
 email1.send_keys("test@gmail.com")
 chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_0 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//button[@name='jetpack_subscriptions_widget']").click()
#left email

name1=chrome.find_element_by_id("et_pb_contact_name_0")
name1.send_keys("Igor")
email11=chrome.find_element_by_id("et_pb_contact_email_0")
email11.send_keys("test11@gmail.com")
message11=chrome.find_element_by_id("et_pb_contact_message_0")
message11.send_keys("Hello!")
captcha11=chrome.find_element_by_xpath("//div[@id='et_pb_contact_form_0']//input[@class='input et_pb_contact_captcha']")
captcha11.send_keys("17")
chrome.find_element_by_xpath("//div[@id='et_pb_contact_form_0']//button[@class='et_pb_contact_submit et_pb_button']").click()
#form1

username1=chrome.find_element_by_id("user_login_5cf0292fc8ea4")
username1.send_keys("Igor")
password1=chrome.find_element_by_id("user_pass_5cf0292fc8ea4")
password1.send_keys("123qwe")
chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_login et_pb_login_0 et_pb_newsletter clearfix et_pb_bg_layout_dark  et_pb_text_align_left']//button[@type='submit']").click()
#form2

chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_toggleet_pb_toggle_0 et_pb_toggle_item et_pb_toggle_close']/h5[@class='et_pb_toggle_title']").click()
#a toogle

name22=chrome.find_element_by_id("et_pb_contact_name_1")
name22.send_keys("Igor")
email22=chrome.find_element_by_id("et_pb_contact_email_1")
email22.send_keys("test22@gmail.com")
message22=chrome.find_element_by_id("et_pb_contact_message_1")
message22.send_keys("Hello!")
captcha22=chrome.find_element_by_xpath("//div[@id='et_pb_contact_form_1']//input[@class='input et_pb_contact_captcha']")
captcha22.send_keys("14")
chrome.find_element_by_xpath("//div[@id='et_pb_contact_form_1']//button[@class='et_pb_contact_submit et_pb_button']").click()
#form3

username2=chrome.find_element_by_id("user_login_5cf0292fcc10d")
username2.send_keys("Igor")
password2=chrome.find_element_by_id("user_pass_5cf0292fcc10d")
password2.send_keys("123zxc")
chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_login et_pb_login_1 et_pb_newsletter clearfix et_pb_bg_layout_dark  et_pb_text_align_left']//button[@class='et_pb_newsletter_button et_pb_button']").click()
#form4

name33=chrome.find_element_by_name("et_pb_contact_name_2")
name33.send_keys("Igor")
email33=chrome.find_element_by_name("et_pb_contact_email_2")
email33.send_keys("test33@gmail.com")
message33=chrome.find_element_by_name("et_pb_contact_message_2")
message33.send_keys("Hello!")
captcha33=chrome.find_element_by_xpath("//div[@id='et_pb_contact_form_2']//input[@class='input et_pb_contact_captcha']")
captcha33.send_keys("25")
chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_contact_form_2 et_pb_contact_form_container clearfix']//button[@type='submit']").click()
#form4

input2=chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_1 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//input[@type='text']")
input2.send_keys("Igor")
chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_1 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//input[@id='searchsubmit']").click()
#right Search

chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_1 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//img[@class='widgets-list-layout-blavatar']").click()
 #right icon

chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_1 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//a[@class='bump-view']").click()
 #right link

email2=chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_1 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//input[@type='email']")
email2.send_keys("test@gmail.com")
chrome.find_element_by_xpath("//div[@class='et_pb_module et_pb_sidebar_1 et_pb_widget_area et_pb_bg_layout_light clearfix et_pb_widget_area_left']//button[@name='jetpack_subscriptions_widget']").click()
#right email