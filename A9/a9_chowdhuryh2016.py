import csv


def make_data_set(file_name):
    # read data set from specified file
    # return list of tuples in format: 8 attributes, diagnosis
    input_set_list = []
    fields = [] # intialize the titles

    # read csv file
    with open(file_name, 'r') as inputfile:
        inputfile_reader = csv.reader(inputfile) # create a csv reader object
        fields = next(inputfile_reader) # extract field names through the first row

        # extract each data row 
        for row in inputfile_reader:
            # get each attribute and diagnosis for a patient and create a tuple
            patient_tuple = int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), \
                float(row[5]), float(row[6]), int(row[7]), int(row[8])
            # print("patient_tuple ", patient_tuple)
            input_set_list.append(patient_tuple) # append tuple to list
        # print(input_set_list)
        
    return input_set_list


# element-by-element sums of two lists of 7 items
def sum_lists(list1, list2):
    sums_list = []
    for index in range(7):
        sums_list.append(list1[index] + list2[index])
    return sums_list


# convert each list element into an average by dividing by the total
def make_averages(sums_list, total_int):
    averages_list = []
    for value_int in sums_list:
        averages_list.append(value_int / total_int)
    return averages_list


# build a classifier using the training set
def train_classifier(training_set_list):
    nondiabetic_sums_list = [0] * 8 # list of sums of nondiabetic attributes
    nondiabetic_count = 0 # count of nondiabetic patients
    diabetic_sums_list = [0] * 8 # list of sums of diabetic attributes
    diabetic_count = 0 # count of diabetic patients

    for patient_tuple in training_set_list:
        if patient_tuple[8] == 0: # if nondiabetic diagnosis
            # add nondiabetic attributes to nondiabetic total
            nondiabetic_sums_list = sum_lists(nondiabetic_sums_list, patient_tuple[0:8])
            nondiabetic_count += 1
        else: # else diabetic diagnosis
            # add diabetic attributes to diabetic total
            diabetic_sums_list = sum_lists(diabetic_sums_list, patient_tuple[0:8])
            diabetic_count += 1

    # print("nondiabetic_sums_list ", nondiabetic_sums_list, "\ndiabetic_sums_list ", diabetic_sums_list)
    # find averages of each set of nondiabetic or diabetic attributes
    nondiabetic_averages_list = make_averages(nondiabetic_sums_list, nondiabetic_count)
    diabetic_averages_list = make_averages(diabetic_sums_list, diabetic_count)
    # print("nondiabetic_averages_list ", nondiabetic_averages_list, "\ndiabetic_averages_list ", diabetic_averages_list)
    # seperator values for each attribute averages nondiabetic and diabetic
    classifier_list = make_averages(sum_lists(nondiabetic_averages_list, diabetic_averages_list), 2)
    # print("classifier_list ", classifier_list)
    return classifier_list


def classify_test_set(test_set_list, classifier_list):
    result_list = []
    for patient_tuple in test_set_list:
        benign_count = 0
        malignant_count = 0
        id_str, diagnosis_str = patient_tuple[:2]
        for index in range(9):
            if patient_tuple[index + 2] > classifier_list[index]:
                malignant_count += 1
            else:
                benign_count += 1
        print(diagnosis_str)
        result_tuple = (id_str, benign_count, malignant_count, diagnosis_str)
        result_list.append(result_tuple)
    return result_list


def report_results(result_list):
    total_count = 0
    inaccurate_count = 0
    for result_tuple in result_list:
        benign_count, malignant_count, diagnosis_str = result_tuple[1:4]
        total_count += 1
        if (benign_count > malignant_count) and (diagnosis_str == "m"):
            inaccurate_count += 1
        elif diagnosis_str == "b":
            inaccurate_count += 1
    print(
        "Of ", total_count, " patients, there were ", inaccurate_count, " inaccuracies"
    )


def main():
    print("Reading in training data...")
    training_file = "test_data.csv"
    training_set_list = make_data_set(training_file)
    print("Done reading training data. \n")


    print("Training classifier...")
    classifier_list = train_classifier(training_set_list)
    print("Done training classifier. \n")

#   print("Reading in test data...")
#   test_file = "test_data.txt"
#   test_set_list = make_data_set(test_file)
#   print("Done reading test data. \n")

#   print("Classifying records...")
#   result_list = classify_test_set(test_set_list, classifier_list)
#   print("Done classifying. \n")

#   report_results(result_list)
#   print("Program finished.")

main()
