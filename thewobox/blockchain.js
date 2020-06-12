
//TODO: peer-to-peer network to communicate with other nodes, real proof-of-work according to bitcoin wiki 
//TODO: merkle tree for data transactions, replaceChain method, data object is not showing, timestamp 
//TODO: increase the amount of difficulty after a specific number of block has been mined 
//NOTE: Every node in the network holds a copy of the blockchain

// npm install --save body-parser crypto-js ws express

const SHA256 = require('crypto-js/sha256');
const express = require("express");
const bodyParser = require('body-parser');
const WebSocket = require("ws");
var http_port = process.env.HTTP_PORT || 3001;
var p2p_port = process.env.P2P_PORT || 6001;
var initialPeers = process.env.PEERS ? process.env.PEERS.split(',') : [];

class Block{
	constructor(index = '', timestamp = '', data, previousHash = ''){
		this.index = index;
		this.timestamp = timestamp;
		this.data = data;
		this.previousHash = previousHash;
		this.hash = this.calculateHash();
		this.nonce = 0;
	}

	calculateHash(){
		return SHA256(this.index + this.previousHash + this.timestamp + JSON.stringify(this.data) + this.nonce).toString();
	}

	mineBlock(difficulty){
		while(this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")){
			this.nonce++;
			this.timestamp = new Date().getTime()/1000;
			this.hash = this.calculateHash();
		}

		console.log("Block Mined!! " + this.hash);
	}
}

class Blockchain{
	constructor(){
		this.chain = [this.createGenesisBlock()];
		this.difficulty = 2;
	}

	createGenesisBlock(){
		return new Block(0, new Date().getTime()/1000, "Genesis Block", "0");
	}

	getLatestBlock(){
		return this.chain[this.chain.length-1];
	}

	addBlock(newBlock){
		newBlock.index = this.getLatestBlock().index + 1;
		newBlock.previousHash = this.getLatestBlock().hash;
		newBlock.mineBlock(this.difficulty);
		console.log("Checking block validation...")
		if(this.isValidBlock(newBlock, this.getLatestBlock())){
			this.chain.push(newBlock);	
		}
	}

	isValidBlock(newBlock, previousBlock){
		if(previousBlock.index + 1 !== newBlock.index){
			console.log("Invalid index");
			return false;
		} else if(previousBlock.hash !== newBlock.previousHash){
			console.log("Invalid previousHash");
			return false;
		} else if (newBlock.calculateHash() !== newBlock.hash) {
        	console.log(typeof (newBlock.hash) + ' ' + typeof newBlock.calculateHash());
        	console.log('Invalid hash: ' + newBlock.calculateHash() + ' ' + newBlock.hash);
        	return false;
    	}
			return true;
	}

	isChainValid(){
		for(let i = 1; i<this.chain.length; i++){
			const currentBlock = this.chain[i];
			const previousBlock = this.chain[i - 1];

			if(currentBlock.hash !== currentBlock.calculateHash()){
				return false;
			}

			if(currentBlock.previousHash !== previousBlock.hash){
				return false;
			}
		}

		return true;
	}

}

let vocfuCoin = new Blockchain();
console.log("Mining Block 1....");
vocfuCoin.addBlock(new Block({amount: 4}));
console.log("Mining Block 2....");
vocfuCoin.addBlock(new Block({amount: 10}));
console.log("Mining Block 3....");
vocfuCoin.addBlock(new Block({amount: 20}));
console.log("Mining Block 4....");
vocfuCoin.addBlock(new Block({amount: 50}));
console.log(JSON.stringify(vocfuCoin, null, 4));
console.log('Checking Blockchain validation... ');
if(vocfuCoin.isChainValid()){
	console.log('SUCCESS: Blockchain is valid!');
}
console.log("Changing Blockchain form...");
vocfuCoin.chain[1].data = {amount: 100};
vocfuCoin.chain[1].hash = vocfuCoin.chain[1].calculateHash();
if(!vocfuCoin.isChainValid()){
	console.log('ERROR: Blockchain is not valid any more.');
}



