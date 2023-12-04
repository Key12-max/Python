
class Character {
    constructor(name){
        this.name= name
        this.health= 100
        this.strength= 50
        this.isAlive = true
        this.weapons = []
        this.equipped_weapon = null
    }
    //select a weapon
    pick_up=(weapon)=>{
        this.weapons.push(weapon)
        return this
    }
    //this is checking our weapon that we select at first
    equip_weapon=(weapon_index)=>{
        this.equipped_weapon=this.weapons[weapon_index]
        return this

    }
    //attack method
    attack=(target)=>{
        target.health-=this.strength*this.equipped_weapon.damage
        console.log(target.health)
        return this
    }
}
export default Character