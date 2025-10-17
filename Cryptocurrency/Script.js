const globalStats = {
  "Total Cryptocurrencies": "33,316",
  "Total Exchanges": "169",
  "Total Market Cap": "1.7T",
  "Total 24h Volume": "181.4B",
  "Total Markets": "39.8K"
};

const topCoins = [
  { name: "Bitcoin (BTC)", price: "$42,000", cap: "$800B", change: "4%" },
  { name: "Ethereum (ETH)", price: "$3,200", cap: "$380B", change: "3%" },
  { name: "Tether USD (USDT)", price: "$1.00", cap: "$68B", change: "0%" },
  { name: "Binance Coin (BNB)", price: "$280", cap: "$45B", change: "2%" },
  { name: "Solana (SOL)", price: "$100", cap: "$35B", change: "5%" },
  { name: "XRP", price: "$0.75", cap: "$32B", change: "1%" },
  { name: "Cardano (ADA)", price: "$1.20", cap: "$40B", change: "2%" },
  { name: "USD Coin (USDC)", price: "$1.00", cap: "$50B", change: "0%" },
  { name: "Avalanche (AVAX)", price: "$90", cap: "$24B", change: "3%" },
  { name: "Polkadot (DOT)", price: "$25", cap: "$28B", change: "4%" }
];

const statsContainer = document.getElementById("global-stats");
const coinContainer = document.getElementById("coin-list");

Object.entries(globalStats).forEach(([title, value]) => {
  const card = document.createElement("div");
  card.className = "stat-card";
  card.innerHTML = `<h3>${title}</h3><p>${value}</p>`;
  statsContainer.appendChild(card);
});

topCoins.forEach(coin => {
  const card = document.createElement("div");
  card.className = "coin-card";
  card.innerHTML = `
    <h3>${coin.name}</h3>
    <p>Price: ${coin.price}</p>
    <p>Market Cap: ${coin.cap}</p>
    <p>Daily Change: ${coin.change}</p>
  `;
  coinContainer.appendChild(card);
});
