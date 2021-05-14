function name_to_number(name) {
    var answer;
    switch(name) {
        case 'Rock':
            answer = 0;
            break;
        case 'Spock':
            answer = 1;
            break;
        case 'Paper':
            answer = 2;
            break;
        case 'Lizard':
            answer = 3;
            break;
        case 'Scissors':
            answer = 4;
            break;    
        default:
            answer = "Error";
    }
    return answer;
}
function number_to_name (number){
    var answer;
    switch(number) {
        case 0:
            answer = 'Rock';
            break;
        case 1:
            answer = 'Spock';
            break;
        case 2:
            answer = 'Paper';
            break;
        case 3:
            answer = 'Lizard';
            break;
        case 4:
            answer = 'Scissors';
            break;    
        default:
            answer = "Error";
    }
    return answer;
}
function rspls(player_choice) {
    var comp_c = document.createElement("img");
    var player_c= document.createElement("img");
    comp_c.width = 150;
    comp_c.height = 150;
    player_c.width = 150;
    player_c.height = 150;
    var choises = {
        0: "static/img/stones.png",
        1: 'static/img/spock.png',
        2: 'static/img/old-paper.png',
        3: 'static/img/lizard.png',
        4: 'static/img/scissors.png'
    }
    var wins = [['', 'vapotites', 'covers', 'crushes', 'crushes'],
                ['vapotites', '', 'disproves', 'poisons', 'smashes'],
                ['covers', 'disproves', '', 'eats', 'cut'],
                ['crushes', 'poisons', 'eats', '', 'decapitate'],
                ['crushes','smashes','cut','decapitate','']]
    var player_number = name_to_number(player_choice);
    var comp_number = Math.floor(Math.random() * 5);
    var comp_choice = number_to_name(comp_number);
    
    comp_c.id = 'image';
    comp_c.src = choises[comp_number];

    player_c.id = 'image_p';
    player_c.src = choises[player_number];
    var comp_src = document.getElementById('computer_choice');
    var player_src = document.getElementById('player_choice');
    if (document.getElementById('image')){
        comp_src.removeChild(document.getElementById('image'));
    }
    if (document.getElementById('image_p')){
        player_src.removeChild(document.getElementById('image_p'));
    }

    comp_src.appendChild(comp_c);
    player_src.appendChild(player_c);
    document.getElementById("user_choice").innerHTML=('You choose '+player_choice);

    var result = player_number - comp_number;
    console.log(result);
    console.log('Computer chooses '+comp_choice);
    document.getElementById("comp_choice").innerHTML=('Computer chooses '+comp_choice);


    if ((result % 5) == 1 || (result % 5) == 2 || (result % 5) == -3 || (result % 5) == -4){
        document.getElementById("result").innerHTML='Player wins!';
        document.getElementById("winner").innerHTML=(player_choice +' '+ wins[player_number][comp_number]+ ' '+ comp_choice + '!');

    }else if ((result % 5) == 3 || (result % 5) == 4 || (result % 5) == -1 || (result % 5) == -2) {
        document.getElementById("result").innerHTML='Computer wins!';
        document.getElementById("winner").innerHTML=(comp_choice +' '+ wins[comp_number][player_number]+ ' '+ player_choice + '!');

    }else if ((result % 5) == 0){
        document.getElementById("result").innerHTML="It's a tie!";
        document.getElementById("winner").innerHTML="";

        
    }else{
        document.getElementById("result").innerHTML="Please choose properly";
    }
    //document.getElementById("click").submit();
}
console.log('JS loaded')