import Character from './character.js';
import Weapon from './weapons.js';

let deff = new Character('Deff')
//console.log(deff)
let kit = new Character('Kit kat')
//console.log(kit)
//let create a weapon
let raffle = new Weapon('raffle','super_rafle',.2,10,2)
let kit_rafle = new Weapon('kitty','kit_kat_rafle',.3,20,3)

deff.pick_up(raffle)
deff.equip_weapon(0)
kit.pick_up(kit_rafle)
kit.equip_weapon(0)


//kit.attack(deff).attack(deff).attack(deff).attack(deff)
//console.log(deff)
//console.log(kit)
kit.drop_weapon(kit_rafle)
console.log(kit)
