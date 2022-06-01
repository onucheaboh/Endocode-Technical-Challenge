from flask import Flask, request
import re

app= Flask(__name__)


#app.route('/helloworld')
#def helloworld():
#   return "Hello Stranger..."
@app.route('/helloworld', methods=['GET'])
def helloworldname():
  name = request.args.get('name')
  if name:
    #splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', name)).split()
    seperated_name = re.sub("([A-Z])", " \\1", name).strip()
    return "Hello %s" % seperated_name
   else:
    return "Hello Stranger"

 @app.route('/versionz')
 def projectname():
    return "Hello Stranger"


    if __name == '__main__':
      app.run(debug=True, port=8080)
