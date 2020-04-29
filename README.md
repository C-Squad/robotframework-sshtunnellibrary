NOTE: Robot framework SSH Library is now having SSH tunnel functionality so it is not necessary to use this library with it. however it is still can be used with other `connection` based libraries like REST API, Database, Seleneium etc.

# robotframework-sshtunnellibrary

SSHTunnelLibrary is a Robotframework library to support SSHTunnels. It will help to connect to remote host using SSH Local Forwarding.

[![Build Status](https://travis-ci.com/C-Squad/robotframework-sshtunnellibrary.svg?branch=master)](https://travis-ci.com/C-Squad/robotframework-sshtunnellibrary)
[![Build Status](https://img.shields.io/pypi/l/robotframework-sshlibrary.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## Usage
Install robotframework-sshtunnellibrary and its dependencies via pip

```
pip install -U sshtunnel
pip install -U robotframework-sshtunnellibrary
```

## Example

SSH Tunnel Library can be used with libraries like SSHLibrary, RequestLibrary, DatabaseLibrary, SeleniumLibrary to make connection to ssh, rest api, database connection, web application respectively. 

Here is an example to make SSH connection using request library via SSH Server.

``` robotframework
*** Settings ***
Library  SSHTunnelLibrary
Library  SSHLibrary

*** Variables ***
${REMOTE_HOST}=  <Remote_IP/Name>
${REMOTE_PORT}=  22 
${SSH_SERVER}=  <SSH_Server_IP/Name>
${SSH_SERVER_PORT}=  22
${SSH_SERVER_USERNAME}=  <SSH_Server_Username>
${SSH_SERVER_PASSWORD}=  <SSH_Server_Password>
${LOCAL_HOST}=  localhost
${LOCAL_PORT}=  0

${REMOTE_USERNAME}=  <Remote_host_Username>
${REMOTE_PASSWORD}=  <Remote_host_Password>

*** Test Cases ***
SSH Connection using SSH Tunnel
    # Create Tunnel
    Start SSH Tunnel  MySshTunnel  ${REMOTE_HOST}  ${REMOTE_PORT}  ${SSH_SERVER}  ${SSH_SERVER_PORT}  ${SSH_SERVER_USERNAME}  ${SSH_SERVER_PASSWORD}  ${LOCAL_HOST}  ${LOCAL_PORT}
    ${LOCAL_BIND_PORT}=  Get Local Port
    
    # Connection using local bind
    Open Connection     ${LOCAL_HOST}  port=${LOCAL_BIND_PORT}
    Login               ${REMOTE_USERNAME}        ${REMOTE_PASSWORD}

    # Closing the Tunnel
    Stop SSH Tunnel  MySshTunnel
```
