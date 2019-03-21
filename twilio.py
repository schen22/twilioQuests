from flask import Flask, send_from_directory, make_response, render_template
# from twilio import twiml
import xml.etree.ElementTree as ET 

app = Flask(__name__, static_folder='xml', static_url_path='/')

# reading xml from disk
twiml = ET.parse('xml/twilio.xml')
root = twiml.getroot()
print root.tag
for child in root:
    print child.tag, child.attrib


@app.route('/')
def hello_twilio():
    return 'Hello, world!'

@app.route('/inbound')
def twilio_response():
    response = make_response(open("xml/twilio.xml").read())
    response.headers['Content-Type'] = 'application/xml'
    return response
    #return send_from_directory('xml', 'twilio.xml', as_attachment=True)
    #number = request.form['From']
    #message_body = request.form['Body']

    #resp = twiml.Response()
    #resp.message('Hello world!'.format(number, message_body))
    #return str(resp)
