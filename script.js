const url = 'https://gorest.co.in/public/v1/users';
const token = 'd7c01847de4c083cb154e9a533294301e9f05f93dbae7d589e42ece63226c0a3';

fetch(url, {
    headers: {
        Authorization: `token ${token}`
    }
}).then(res => res.json()).then(json => console.log(json));