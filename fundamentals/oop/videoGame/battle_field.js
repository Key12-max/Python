import Character from './character.js';
import Weapon from './weapons.js';

let deff = new Character('Deff')
//console.log(deff)
let kit = new Character('Kit kat')
//console.log(kit)
//let create a weapon
let raffle = new Weapon('Raffle','super_rafle',2,10)
let kit_rafle = new Weapon('kitty','kit_kat_rafle',3,20)

deff.pick_up(raffle)
deff.equip_weapon(0)
kit.pick_up(kit_rafle)
kit.equip_weapon(0)

kit.attack(deff)
//console.log(deff)
//console.log(kit)
