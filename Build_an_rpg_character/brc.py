full_dot = '●'
empty_dot = '○'
name = ""

def create_character(name,strength,intelligence,charisma):

    if not isinstance(name, str):
        return "The character name should be a string"
    if not name:
        return "The character should have a name"
    if len(name)>10:
       return "The character name is too long"
    if ' ' in name:
      return "The character name should not contain spaces"
    stats = {'STR': strength,'INT': intelligence, 'CHA': charisma}
    for stat in stats.values():
        if not isinstance(stat, int):
            return "All stats should be integers"
    for stat in stats.values():
        if stat < 1:
            return "All stats should be no less than 1"
    for stat in stats.values():
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(stats.values()) != 7 :
        return "The character should start with 7 points"

    character_string = name
    for key in ['STR', 'INT', 'CHA']:
        stat = stats[key]
        character_string += f'\n{key} {full_dot*stat}{empty_dot*(10-stat)}'

    return character_string
create_character('ren', 4, 2, 1)
