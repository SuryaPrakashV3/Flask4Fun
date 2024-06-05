class NamedAPIResourceList[T]:
    '''The total number of resources available from this API.'''
    count: int
    '''The URL for the next page in the list.'''
    next: str
    '''The URL for the previous page in the list.'''
    previous: str	
    '''A list of named API resources.'''
    results: list[T]


class Pokemon:
    '''The identifier for this resource.'''
    id: int
    '''The name for this resource.'''
    name: str	
    '''The base experience gained for defeating this Pokémon.'''
    base_experience: int
    '''The height of this Pokémon in decimetres.'''
    height: int
    '''Set for exactly one Pokémon used as the default for each species.'''
    is_default: bool
    '''Order for sorting. Almost national order, except families are grouped together.'''
    order: int
    '''The weight of this Pokémon in hectograms.'''
    weight: int
    '''A list of abilities this Pokémon could potentially have.'''
    # list PokemonAbility
    abilities: list

    '''A list of forms this Pokémon can take on.'''
    # list NamedAPIResource (PokemonForm)
    forms: list
    '''A list of game indices relevent to Pokémon item by generation.'''
    # list VersionGameIndex
    game_indices: list	
    '''A list of items this Pokémon may be holding when encountered.'''
    # list PokemonHeldItem
    held_items: list
    '''A link to a list of location areas, as well as encounter details pertaining to specific versions.'''
    location_area_encounters: list	
    '''A list of moves along with learn methods and level details pertaining to specific version groups.'''
    # list PokemonMove
    moves: list
    '''A list of details showing types this pokémon had in previous generations'''
    # list PokemonTypePast
    past_types: list
    '''A set of sprites used to depict this Pokémon in the game. A visual representation of the various sprites can be found at PokeAPI/sprites'''
    # PokemonSprites
    sprites: any
    '''A set of cries used to depict this Pokémon in the game. A visual representation of the various cries can be found at PokeAPI/cries'''
    # PokemonCries
    cries: any
    '''The species this Pokémon belongs to.'''
    # NamedAPIResource (PokemonSpecies)
    species: any
    '''A list of base stat values for this Pokémon.'''
    # list PokemonStat
    stats: list
    '''A list of details showing types this Pokémon has.'''
    # list PokemonType
    types: list

Resources = {'pokemon': 'pokemon'}