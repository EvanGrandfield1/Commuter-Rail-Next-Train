import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin', default=None, type=str, help='from')
    parser.add_argument('--to', default=None, type=str, help='to')
    args = parser.parse_args()
    return args

### Check if have proper command line arguments in order to proceed ###
args = parse_arguments()



driver = webdriver.Chrome()
driver.get("https://www.mbta.com/trip-planner") 

inputElement_0 = driver.find_element_by_id("from")
inputElement_0.send_keys(args.origin)

inputElement_1 = driver.find_element_by_id("to")
inputElement_1.send_keys(args.to)

inputElement_2 = driver.find_element_by_id("trip-plan__submit")
inputElement_2.send_keys(Keys.ENTER)

all_times = driver.find_elements_by_class_name('trip-plan-itinerary-length-time')

for time in all_times:
    print(time.text)

if len(all_times) == 0:
	print('error')

driver.close()