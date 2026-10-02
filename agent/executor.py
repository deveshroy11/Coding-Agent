import subprocess
import tempfile
import os 

from langchain_core.tools import tool 
from subprocess import TimeoutExpired

@tool
def execute_cpp(code:str,test_input: str)->str:
    """
    Compile and execute C++17 code.
    Returns compilation errors, runtime errors, or program output.
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = os.path.join(temp_dir, "main.cpp")
        executable=os.path.join(temp_dir,"main")

        with open(source_file,"w") as f:
            f.write(code)

        #compile 

        compile_result= subprocess.run(
            ["g++", "-std=c++17", "-fuse-ld=bfd", source_file, "-o", executable],
            capture_output=True,
            text = True
        )

        if compile_result.returncode!=0:
            return f"COMPILATION_ERROR:\n{compile_result.stderr}"

        #run

        # run_result = subprocess.run(
        #     [executable],
        #     capture_output=True,
        #     text = True,
        #     timeout = 5            
        # )

        # if run_result.returncode!=0:
        #     return f"Runtime_Error:\n{run_result.stderr}"

        try:
            run_result = subprocess.run(
                [executable],
                input = test_input,
                capture_output= True,
                text = True,
                timeout = 5
            )
        except TimeoutExpired:
            return "TIMEOUT_ERROR:\nProgram exceeded the 5 second limit."

        if run_result.returncode != 0:
            return f"RUNTIME_ERROR:\n{run_result.stderr}"

        return f"SUCCESS:\n{run_result.stdout}"