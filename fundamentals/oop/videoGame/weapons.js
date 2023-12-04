class Weapon{
    constructor(name, type, damage, weight,use_count){
        this.name = name
        this.type = type
        this.damage = damage
        this.waight = weight
        this.use_count = use_count

    }
    use_new_weapon=()=>{
        this.use_count--
        return this
    }
}
export default Weapon