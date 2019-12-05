# fb_dynamicconv
Extraction and adaptation to python 3.7+ of Facebook FairSeq DynamicConv

Fairseq has a dependency to *sacrebleu* which depends on other packages such as typing 
which produce a problem with python >=3.7.

Also the module for Dynamic Convolution does not have the correct imports having a few issues:

    import fairseq.modules.dynamicconv_layer
    ---------------------------------------------------------------------------
    ModuleNotFoundError                       Traceback (most recent call last)
    <ipython-input-7-a398363c1102> in <module>
    ----> 1 import fairseq.modules.dynamicconv_layer
    
    ModuleNotFoundError: No module named 'fairseq.modules.dynamicconv_layer'
    
This package tries to fix this and make the Dynamic Convolution package independent from the rest of fairseq.

The license is just the same as the fairseq license 