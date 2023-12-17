import time
import random

class Co_ordinator:
    def _init_(self, participants):
        self.participants = participants
        
    def send_prepare(self):
        votes = []
        
        for participant in self.participants:
            try:
                vote = participant.prepare()
                votes.append(vote)
            except Exception as e:
                print("Error in sending prepare message to participant: ", str(e))
                self.send_abort()
                
        if all(votes):
            self.send_commit()
        else:
            self.send_abort()
            
            
    def send_commit(self):
        
        for participant in self.participants:
            try:
                participant.commit()
            except Exception as e:
                print("Error in sending commit message to participant: ", str(e))
                self.send_abort()
                
    
    def send_abort(self):
        
        for participant in self.participants:
            try:
                participant.abort()
            except Exception as e:
                print("Error in sending abort message to participant: ", str(e))
                
class Participant:
    def _init_(self, name):
        self.name = name
        
    def prepare(self):
        print("Participant ", self.name, " Prepare Phase")
        
        time.sleep(random.uniform(0.5, 1.5))
        
        return True
    
    def commit(self):
        print("Participant ", self.name, " Commit Phase")
        
        time.sleep(random.uniform(0.5, 1.5))
        
        pass
    
    def abort(self):
        print("Participant ", self.name, " Abort Phase")
        
        time.sleep(random.uniform(0.5, 1.5))
        
        pass
    
    
    
if __name__ == "__main__":
    participant1 = Participant('1')
    participant2 = Participant('2')
    
    co_ordinator = Co_ordinator([participant1, participant2])
    
    try:
        co_ordinator.send_prepare()
        
        print("Transaction successful")
        
    except Exception as e:
        print("Aborted ")