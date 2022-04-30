import http from 'k6/http';
import { sleep, check } from 'k6';
import { randomItem } from 'https://jslib.k6.io/k6-utils/1.1.0/index.js';

export const options = {
    // stages: [
    //     {duration: '20s', target: 100},    
    //     {duration: '10s', target: 300},
    //     {duration: '59s', target: 300},
    //     {duration: '10s', target: 100},
    //     {duration: '10s', target: 0}
    // ],
    stages: [
            {duration: '1s', target: 100},            
            {duration: '59s', target: 100}                         
        ],
    thresholds: {
        'http_req_duration': ['p(99)<1000'], // 99% of requests must complete below 1.5s
        'logged in successfully': ['p(99)<1000'], // 99% of requests must complete below 1.5s
    }
}

const names = ['BURRO', 'PILHA', 'TESTE', 'CASPA', 'URROS'];

const BASE_URL = 'http://0.0.0.0:85';

export default function () {

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const randomName = randomItem(names);
    const res = http.post(`${BASE_URL}`, `{"word": "${randomName}"}`, params);   
    const states = ['HALF', 'RIGHT', 'WRONG'];

    const checkRes = check(res, {        
        'status is 200': (r) => r.status === 200,        
        'response letters': (r) => r.json().letters,
        'response 1': (r) => states.includes(r.json()['letters']['0']['state']),
        'response 2': (r) => states.includes(r.json()['letters']['1']['state']),
        'response 3': (r) => states.includes(r.json()['letters']['2']['state']),
        'response 4': (r) => states.includes(r.json()['letters']['3']['state']),
        'response 5': (r) => states.includes(r.json()['letters']['4']['state']),
    });
}