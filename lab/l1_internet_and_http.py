# 1. Internet and HTTP


# server - tam kydeto stoqt resursite
# client - koito iska resursite

# network protokol - nachin po koito nie komunikirame mejdu razlichnite device-i
# htp e network protocol - na principa request / response

# packet - small chunks of data sent over networks
# header - important info inside packets (contents, origin, destination)

# IP Address - unique id of the device in a specific network

# IPv4
# 192.168.1.18 - vseki ot komponentite e 8 bita
# 1 - subnetwork: podmreja
# 18 - konkreten device

# IPv6 sa poveche komponenti

# DNS - Domain Name Server
# the human way to access an IP
# softuni.bg == 217.174.159.34:443


# ------------------------------------------------------------------------
# HTTP - za web
# https - +encryptva danni

# POST - create / store a result
# GET - Read / retrieve a resource
# PUT - Update / modify a resource
# DELETE - Delete / remove a resource

# these verbs make the CRUD operations
# Create, Read, Update, Delete

# HEAD - vryshta metadannite
# OPTIONS - dadeniq klient kakvi prava ima


# HTTP 2.0 - posledna versiq - na 50% ot saitovete - syvmestimo s HTTP 1.1


# ------------------------------------------------------------------------
"""
URL - Uniform Resource Locator


reference to web resource that specifies its location on a network
unikalno za 1 mreja

HOST == ime na domaina
HTTP - port 80
HTTPS - port 443

query - kakvo tyrsim
fragment - element ot stranicata


safe url characters: [0-9a-zA-Z], $, -, _, ., +, *, ', (, ), ,, !
simvolite ot kirilicata ne sa validni i se enkodvat
ostanalite simvoli znachat neshto drugo

"""

# ------------------------------------------------------------------------
"""
Dev Tools - v browser-a
"""

# ------------------------------------------------------------------------
"""
MIME - multi-Purpose Internet Mail Extensions
Internet standard for encoding resources
{type}/{subtype} i.e. text/plain
"""

# ------------------------------------------------------------------------
"""
HTTP request

<method> <resource> HTTP/<version>    # GET /../.. HTTP/1.1
<headers>
empty line
<body>                                # naprimer za PORT e username i pass pri log in
                                      # pri POST i HTTPS body-to se kriptira

HTTP response codes:

1xx - informational
2xx - successful: 200 - ok, 201 - created
3xx - redirection
4xx - client error
5xx - server error

"""











