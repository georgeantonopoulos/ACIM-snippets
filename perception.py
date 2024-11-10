class Perception:
    def __init__(self):
        self.thoughts = []
        self.reality = None
        self.peace_level = 0
        self.forgiveness_applied = False
        
    def add_thought(self, thought):
        """Add a thought to our perception system"""
        self.thoughts.append({
            'content': thought,
            'is_projection': True,
            'has_been_examined': False
        })
        
    def examine_thought(self, thought_index):
        """Examine a thought to see if it's based in reality or projection"""
        if thought_index >= len(self.thoughts):
            return "Thought does not exist"
            
        thought = self.thoughts[thought_index]
        thought['has_been_examined'] = True
        
        # When we examine our thoughts, we increase our peace
        self.peace_level += 1
        return "Thought examined with willingness to see differently"
        
    def apply_forgiveness(self):
        """Apply forgiveness to all current perceptions"""
        if not self.thoughts:
            return "No thoughts to forgive"
            
        for thought in self.thoughts:
            thought['is_projection'] = False
            
        self.forgiveness_applied = True
        self.peace_level += 5
        return "Forgiveness applied, peace increased"
        
    def release_judgment(self):
        """Release all judgments and projections"""
        self.thoughts.clear()
        self.peace_level += 3
        return "All judgments released"
    
    def choose_peace(self):
        """Active choice to align with peace instead of grievances"""
        if self.forgiveness_applied:
            self.peace_level *= 2
            return "Peace multiplied through forgiveness"
        else:
            self.peace_level += 1
            return "Small step toward peace taken"
            
    def get_current_state(self):
        """Return the current state of our perception"""
        return {
            'number_of_thoughts': len(self.thoughts),
            'peace_level': self.peace_level,
            'forgiveness_active': self.forgiveness_applied,
            'examined_thoughts': sum(1 for t in self.thoughts if t['has_been_examined'])
        }

def practice_lesson():
    # Create new perception instance
    my_perception = Perception()
    
    # Add some sample thoughts
    my_perception.add_thought("This person wronged me")
    my_perception.add_thought("The world is against me")
    
    # Practice the lesson
    print("Initial state:", my_perception.get_current_state())
    
    my_perception.examine_thought(0)
    my_perception.examine_thought(1)
    print("After examination:", my_perception.get_current_state())
    
    my_perception.apply_forgiveness()
    print("After forgiveness:", my_perception.get_current_state())
    
    my_perception.choose_peace()
    print("After choosing peace:", my_perception.get_current_state())
    
    my_perception.release_judgment()
    print("Final state:", my_perception.get_current_state())

if __name__ == "__main__":
    practice_lesson()
