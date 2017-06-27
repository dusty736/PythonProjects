# Name: Dustin Burnham
# UW NetID: dusty736
# Section: AB
# CSE 160
# Homework 6: Detecting Fraudulent Data

import csv
import random
import matplotlib.pyplot as plt

################################################################################
# Problem 1: Read and clean Iranian election data
################################################################################

def string_to_int(string_number):
    ""
    
    ""
    
    new_int = string_number.replace(',', '')
    new_int = int(new_int)
    return new_int
    

def extract_election_vote_counts(filename,column_names):
    ""
    
    ""
    
    data = open(filename)
    vote_data = csv.DictReader(data)
    vote_list = []
    for row in vote_data:
        for name in column_names:
            if row[name] != "":
                vote_int = string_to_int(row[name])
                vote_list.append(vote_int)
    data.close()
    return vote_list
    

################################################################################
# Problem 2: Make a histogram
################################################################################

def digit_apart(number):
    ""
    
    ""

    digit_lst = []
    if number > 100:
        number = number % 100
    if len(str(number)) == 1:
        digit_lst.append(0)
        digit_lst.append(number)
    else:
        digit = number / 10
        digit_lst.append(digit)
        digit_lst.append(number % 10)
    return digit_lst
 
     
def digit_fraction(digit_dict,count):
    ""
    
    ""
    
    fraction_lst = []
    for number in digit_dict.keys():
        fraction_lst.append(digit_dict[number] / float(count))
    return fraction_lst


def ones_and_tens_digit_histogram(numbers):
    ""
    
    ""
    
    digit_count = {}
    for val in range(10):
        digit_count[val] = 0
        
    count = 0
    for number in numbers:
        digit_list = digit_apart(number)
        for digit in digit_list:
            digit_count[digit] += 1
            count += 1
    
    fraction_lst = digit_fraction(digit_count, count)
    return fraction_lst
            

################################################################################
# Problem 3: Plot election data
################################################################################

def expected_outcome():
    ""
    
    ""
    
    expected = []    
    for val in range(10):
        expected.append(0.1)
    return expected

def plot_iranian_least_digits_histogram(histogram):
    ""
    
    ""
    
    expected = expected_outcome()
    plt.plot(range(10), histogram, label = "Iran") 
    plt.plot(range(10), expected, label = "Ideal")
    plt.axis([0, 9, 0.06, 0.16])
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.legend()
    #plt.savefig("iran-digits")
    plt.show()


################################################################################
# Problem 4: Smaller samples have more variation
################################################################################

def gen_rand_lst(size_of_list):
    ""
    
    ""
    
    rand_list = []
    for iteration in range(size_of_list):
        rand_list.append(random.randrange(100))
    return rand_list


def plot_distribution_by_sample_size():
    ""
    
    ""
    
    plt.clf()
    hist_dict = {}
    rand_size = [10, 50, 100, 1000, 10000]
    for size in rand_size:
        hist_dict[size] = (ones_and_tens_digit_histogram(gen_rand_lst(size)))
    for size in hist_dict.keys():
        plt.plot(range(10), hist_dict[size], 
                label = str(size) + " random numbers") 
                
    plt.plot(range(10), expected_outcome(), label = "Ideal")
    plt.axis([0, 9, 0, 0.25])
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of last two digits")
    plt.legend()
    plt.savefig("random-digits")
    plt.show()
    

################################################################################
# Problem 5: Comparing variation of samples and Statistics background
################################################################################

def mean_squared_error(numbers1, numbers2):
    ""
    
    ""
    
    assert len(numbers1) == len(numbers2)
    
    MSE = 0
    size_lst = len(numbers1)
    for point in range(size_lst):
        MSE += (numbers1[point] - numbers2[point]) ** 2
    MSE = float(MSE) / size_lst
    return MSE    


################################################################################
# Problem 6: Comparing variatoin of samples Interpreting statistical results
################################################################################

def calculate_mse_with_uniform(histogram):
    ""
    
    ""
    
    return mean_squared_error(histogram,expected_outcome())
    
def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    ""
    
    ""
    
    smaller_count = 0
    larger_or_equal_count = 0
    for sample in range(10000):
        sample = (gen_rand_lst(number_of_iranian_samples))
        sample_hist = ones_and_tens_digit_histogram(sample)
        sample_mse = calculate_mse_with_uniform(sample_hist)
        if sample_mse >= iranian_mse:
            larger_or_equal_count += 1
        else:
            smaller_count += 1
    p_val = float(larger_or_equal_count) / smaller_count
    print "2009 Iranian election MSE:", iranian_mse
    print "Quantity of MSEs larger than or equal to the 2009 \
Iranian election MSE:", larger_or_equal_count
    print "Quantity of MSEs smaller than the 2009 Iranian \
election MSE:", smaller_count
    print "2009 Iranian election null hypothesis rejection level p:", p_val
    print ""
        

################################################################################
# Problem 7: Interpret your results
################################################################################



################################################################################
# Problem 8: Other datasets
################################################################################

def compare_us_mse_to_samples(us_mse, number_of_us_samples):
    ""
    
    ""
    
    smaller_count = 0
    larger_or_equal_count = 0
    for sample in range(10000):
        sample = (gen_rand_lst(number_of_us_samples))
        sample_hist = ones_and_tens_digit_histogram(sample)
        sample_mse = calculate_mse_with_uniform(sample_hist)
        if sample_mse >= us_mse:
            larger_or_equal_count += 1
        else:
            smaller_count += 1
    p_val = float(larger_or_equal_count) / smaller_count
    print "2008 United States election MSE:", us_mse
    print "Quantity of MSEs larger than or equal to the 2008 \
United States election MSE:", larger_or_equal_count
    print "Quantity of MSEs smaller than the 2008 United States \
election MSE:", smaller_count
    print "2008 United States election null \
hypothesis rejection level p:", p_val
    print ""



def compare_general_mse_to_samples(mse, number_of_samples, year, country):
    ""
    
    ""
    
    smaller_count = 0
    larger_or_equal_count = 0
    for sample in range(10000):
        sample = (gen_rand_lst(number_of_samples))
        sample_hist = ones_and_tens_digit_histogram(sample)
        sample_mse = calculate_mse_with_uniform(sample_hist)
        if sample_mse >= mse:
            larger_or_equal_count += 1
        else:
            smaller_count += 1
    p_val = float(larger_or_equal_count) / smaller_count
    print year, country, "election MSE:", mse
    print "Quantity of MSEs larger than or equal to the", year, country, "elec\
tion MSE:", larger_or_equal_count
    print "Quantity of MSEs smaller than the", year, country, "election \
MSE:", smaller_count
    print year, country, "election null hypothesis rejection level p:", p_val
    print ""


def main():
  
    Iran_votes = extract_election_vote_counts("election-iran-2009.csv", 
    ["Ahmadinejad","Rezai", "Karrubi", "Mousavi"])  
    iranian_histogram = ones_and_tens_digit_histogram(Iran_votes)
    #plot_iranian_least_digits_histogram(histogram)
    #plot_distribution_by_sample_size()
    #print mean_squared_error([2, 3, 4], [6, 5, 4])  
    iranian_mse = calculate_mse_with_uniform(iranian_histogram)  
    #compare_iranian_mse_to_samples(iranian_mse, len(Iran_votes))
    
    US_votes = extract_election_vote_counts("election-us-2008.csv", 
    ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])
    US_histogram = ones_and_tens_digit_histogram(US_votes)
    us_mse = calculate_mse_with_uniform(US_histogram)
    #compare_us_mse_to_samples(us_mse, len(US_votes))
    
    compare_general_mse_to_samples(iranian_mse, len(Iran_votes), 2009, "Iranian")    
    compare_general_mse_to_samples(us_mse, len(US_votes), 2008, "United States")
    
    
    
if __name__ == "__main__":
    main()