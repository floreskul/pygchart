import sys
import charts
import function_generator

# wrap the module with an object to be able
# to dynamically generate methods
sys.modules[__name__] = function_generator.ChartFunctionGenerator(
    sys.modules[__name__])
