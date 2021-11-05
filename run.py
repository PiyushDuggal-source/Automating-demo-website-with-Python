from ecom_automation.automation import Automation

with Automation(exiting=False) as auto:
    auto.get_website()
    auto.select_phones_and_quantity(count=4)

    auto.take_screenshot_of_last_pic()
    auto.add_to_cart()
    auto.testing(4)
    auto.select_laptop_and_quantity(count=4)

    auto.take_screenshot_of_last_pic()
    auto.add_to_cart()
    auto.testing(4)
    auto.go_to_cart()
    # auto.checking_out(fname='nameee', lname='nn', companyName='atg', address='kasjdfad', email='test@gmail.com', tele='wdawdawd', city='Delhi', pcode='424823')

