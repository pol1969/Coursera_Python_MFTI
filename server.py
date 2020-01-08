import asyncio
#from collections import defaultdict 


answer = dict()

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port)
 
    server = loop.run_until_complete(coro)
 
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
 
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):


    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
  #      print(f'{resp}')
        self.transport.write(resp.encode())
    
    def process_data(self, data):
        command, corp = data.split(" ", 1)
        corp = corp.strip()
  #      print('command, corp:',command, corp)

        if command =='put':

            key, value, timestamp = corp.split()
            if key not in answer:
                answer[key] = []
            if (int(timestamp), float(value)) not in answer[key]:
                answer[key].append((int(timestamp), float(value)))
 #           print('после добавления',answer) 
            return 'ok\n\n'

        if command =='get':
            ret = 'ok\n'
            s = ''

            if corp =='*':
                for key, value in answer.items():
                    for v in value:
                        s += key
                        s += ' '
                        s += ' '.join([str(ss) for ss in reversed(v)])
                        s += '\n'

    #                print(s)
                s += '\n'
                return ret + s 

            if corp in answer.keys():
                for key, value in answer.items():
                    for v in value:
                        if key == corp:
                            s += key
                            s += ' '
                            s += ' '.join([str(ss) for ss in reversed(v)])
                            s += '\n'

   #             print(s)
                s += '\n'
                return ret + s 


                return 'ok\n{}\n\n'.format(answer[corp])
            else:
                return 'ok\n\n'

        else:
            return 'error\nwrong command\n\n'

if __name__=="__main__":
    run_server('127.0.0.1', 8888)
 
