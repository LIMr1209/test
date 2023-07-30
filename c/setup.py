from distutils.core import setup, Extension
from Cython.Build import cythonize

# python setup.py build_ext --inplace
setup(
    ext_modules=cythonize("uv_compare.pyx"),
)
setup(ext_modules = cythonize(Extension(
    'uv_compare', #生成的动态链接库的名字
    sources=['uv_compare.pyx'], # 里面可以包含 .pyx 文件，以及后面如果我们要调用 C/C++ 程序的话，还可以往里面加 .c / .cpp 文件
    language='c', # 默认就是 c，如果要用 C++，就改成 c++ 就好了
    include_dirs=[], # 这个就是传给 gcc 的 -I 参数
    library_dirs=[],# 这个就是传给 gcc 的 -L 参数
    libraries=[], # 这个就是传给 gcc 的 -l 参数
    extra_compile_args=[], # 就是传给 gcc 的额外的编译参数，比方说你可以传一个 -std=c++11
    extra_link_args=[] # 就是传给 gcc 的额外的链接参数（也就是生成动态链接库的时候用的）
)))