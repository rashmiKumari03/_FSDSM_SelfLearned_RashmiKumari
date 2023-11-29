echo [$(date)]:"START"

echo [$(date)]:"Creating Environment with python 3.8 version....."
conda create -p env python=3.8 -y


echo [$(date)]:"Activating the Environment...."
conda activate ./env    # This might not get activated because window has some issue with git bash ternimal....
                        # Its Better to do this manual.
                        # we can write/run this manually in terminal..as 
                        # source activate ./env     or    conda activate ./env  this will activates our envirnoment.

                        # If any error in activating the env : then update conda here...

echo [$(date)]:"Installing the development requirements...."
pip install -r requirements.txt 


echo [$(date)]:"END"

#To execute this fill write.."bash init_setup.sh" in the bash terminal.

