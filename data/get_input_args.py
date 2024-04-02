#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER:   Megan McLean
# DATE CREATED: 02/04/2024
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse


def get_input_args() -> argparse.Namespace:
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and define these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
      None - simply using argparse module to create & store command line arguments
    Returns:
      parse_args() -data structure that stores the command line arguments object
    """

    parser = argparse.ArgumentParser(description=
                                     """Classifies images using a pretrained CNN model, 
                                        compares the classifications to the true identity of the images, 
                                        and summarises how well the CNN performed on the image classification task.""",
    )
    parser.add_argument("--dir", type=str, default="pet_images/", 
                        help="path to the directory containing the images to be classified")
    parser.add_argument("--arch", type=str, choices=["vgg", "resnet", "alexnet"], default="vgg", 
                        help="the CNN model architecture to use for classification")
    parser.add_argument("--dogfile", type=str, default="dognames.txt", 
                        help="the text file containing the dog names")
    
    return parser.parse_args()
