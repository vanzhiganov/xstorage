FROM centos:7
#  python3-pip
RUN yum install -y epel-release \
    && yum update -y \
    && yum install -y gcc python3 python3-devel python3-setuptools crudini uwsgi uwsgi-plugin-python3 \
    && yum clean all
