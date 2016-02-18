FROM larsilerum/pythonwithgpio
MAINTAINER Lars Larsson <lars.martin.larsson@gmail.com>
ADD . /energilog
WORKDIR /energilog
CMD python energi.py
