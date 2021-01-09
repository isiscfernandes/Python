from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'

print(Geocoder('AIzaSyC7BfPRnhhuUXR9WvDks4qzxlQQMKXDc4s').geocode(endereco).coordinates)
