
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
    //drop weapon
    drop_weapon = (weapon)=>{
        if(weapon == this.equipped_weapon){
            this.equipped_weapon = null
        }
        //lets use filter to use new list of weapons
        this.weapons = this.weapons.filter(lis_el => lis_el = weapon)
        console.log(this.weapons)
        return this
    }
    //attack method
    attack=(target)=>{
        if(this.equipped_weapon.use_count>0){
            target.health-=this.strength*this.equipped_weapon.damage
            console.log(target.health)
            this.equipped_weapon.use_new_weapon()

        } else{
            console.log("Your weapon is broke. Get new one")
        }
        return this
    }
}
export default Character