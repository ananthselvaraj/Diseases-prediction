from cnnClassification import logger
from cnnClassification.utils.exception import CustomException
import sys


try:
    x=1/0
except Exception as e:
    raise CustomException(e,sys)