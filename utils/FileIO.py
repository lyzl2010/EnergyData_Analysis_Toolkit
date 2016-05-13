# -*- coding: utf-8 -*-

import os
import cPickle as pickle
from GlobalParameter import *


class Path:
    def __init__(self):
        pass

    @staticmethod
    def path_checker(directory):
        """

        :param directory:
        :return:
        """
        if os.path.isdir(directory):
            return directory
        else:
            directory = directory.rsplit('/', 1)[0]
            Path.path_checker(directory)


class Load:
    def __init__(self):
        pass

    @staticmethod
    def unpickling(binary_file):
        """

        :param binary_file:
        :return:
        """
        data_dictionary = pickle.load(open(binary_file))

        file_name = binary_file.rsplit('/', 1)[-1]
        file_name = file_name.split('.')[0]
        data_dictionary['file_name'] = file_name

        return data_dictionary

    @staticmethod
    def load_filelist(path):
        """

        :param path:
        :return:
        """
        bin_file_list = []

        try:
            file_names = os.listdir(path)
            for i in xrange(0, len(file_names)):
                ext = os.path.splitext(file_names[i])[-1]
                if ext == '.bin':
                    file = os.path.join(path, file_names[i])
                    bin_file_list.append(file)
        except OSError as err:
            print 'OSError' + str(err)

        return bin_file_list

    @staticmethod
    def print_dictionary(data_dictionary):
        """

        :param data_dictionary:
        :return:
        """
        for i in xrange(0, len(data_dictionary['ts'])):
            print data_dictionary['ts'][i],
            print '\t',
            print data_dictionary['value'][i]


class Save:
    def __init__(self):
        pass

    @staticmethod
    def assure_path(path):
        """

        :param path:
        :return:
        """
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

    @staticmethod
    def dumping_bin(path, data):
        """

        :param path:
        :param data:
        :return:
        """
        f = open(path, 'wb')
        pickle.dump(data, f, 1)
        f.close()

    @staticmethod
    def preprocessed_data2bin_file(data_dictionary):
        """

        :param data_dictionary:
        :return:
        """
        path = Repository_Path
        extra_path = 'preprocessed_data'
        path = os.path.join(path, extra_path)

        Save.assure_path(path)

        preprocessed_binary_file_name = data_dictionary['file_name'] + '.bin'
        preprocessed_binary_file_name = os.path.join(path, preprocessed_binary_file_name)

        Save.dumping_bin(preprocessed_binary_file_name, data_dictionary)

    @staticmethod
    def dependency_model2bin_file(dependency_structure):
        """

        :param dependency_structure:
        :return:
        """
        path = Repository_Path
        extra_path = 'dependency_model'
        path = os.path.join(path, extra_path)

        Save.assure_path(path)

        dependency_binary_file_name = 'dependency_model.bin'
        dependency_binary_file_name = os.path.join(path, dependency_binary_file_name)

        Save.dumping_bin(dependency_binary_file_name, dependency_structure)
