import printing_function
"""
import printing_function as printing
from printing_function import * (不推荐）
from printing_function import print_models as p_m
"""

def main():

    def show_completed_models(completed_models):
        """显示打印好的所有模型"""
        print("\nThe following models have been printed:")
        for completed_model in completed_models:
            print(completed_model)

    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    printing_function.print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)

if __name__ == '__main__':
    main()