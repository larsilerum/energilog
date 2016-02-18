FROM larsilerum/pythonwithgpio
MAINTAINER Lars Larsson <lars.martin.larsson@gmail.com>
ADD energi.py /energilog/
WORKDIR /energilog
CMD python energi.py
