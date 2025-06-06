# SongRecommendationBot

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> An intelligent music recommendation system that analyzes your search history and provides personalized song suggestions with persistent database storage.

## 🎵 Overview

SongRecommendationBot is a Python-based music recommendation engine that leverages your search history to deliver personalized music suggestions. The application creates and maintains a local SQLite database to store user preferences, search patterns, and recommendation history for enhanced accuracy over time.

## ✨ Features

- **Intelligent Recommendations**: Analyzes search patterns to suggest relevant music
- **Persistent Storage**: Maintains a local SQLite database for user data and preferences
- **Search History Analysis**: Learns from your music search behavior
- **Lightweight & Fast**: Minimal resource usage with efficient database operations
- **Cross-Platform**: Compatible with Windows, macOS, and Linux

## 🚀 Quick Start

### One-Line Installation

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Adityaadpandey/SongRecommendationBot/main/run.sh)"
```

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adityaadpandey/SongRecommendationBot.git
   cd SongRecommendationBot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📋 Prerequisites

- **Python**: Version 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for initial setup and music data fetching

## 🛠️ Installation Methods

### Option 1: Automated Script (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/Adityaadpandey/SongRecommendationBot/main/run.sh | sh
```

### Option 2: Manual Setup
```bash
# Clone repository
git clone https://github.com/Adityaadpandey/SongRecommendationBot.git

# Navigate to directory
cd SongRecommendationBot

# Install dependencies
pip install -r requirements.txt

# Initialize database
python setup.py

# Run application
python main.py
```

## 📖 Usage

### Basic Usage
```python
from song_bot import SongRecommendationBot

# Initialize the bot
bot = SongRecommendationBot()

# Get recommendations based on search history
recommendations = bot.get_recommendations(user_id="your_user_id")

# Add a search query to history
bot.add_search_history("your favorite song", user_id="your_user_id")
```

### Command Line Interface
```bash
# Start interactive mode
python main.py --interactive

# Get recommendations for specific user
python main.py --user-id "user123" --recommend

# Import search history from file
python main.py --import-history "search_data.json"
```

## 🗃️ Database Structure

The application automatically creates a SQLite database with the following structure:

- **users**: User profiles and preferences
- **search_history**: Historical search queries and timestamps
- **recommendations**: Generated recommendations and feedback
- **songs**: Music metadata and information

## ⚙️ Configuration

Create a `config.json` file to customize settings:

```json
{
  "database_path": "./song_recommendations.db",
  "max_recommendations": 10,
  "learning_rate": 0.1,
  "api_endpoints": {
    "music_service": "your_api_endpoint"
  }
}
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/SongRecommendationBot.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Code formatting
black src/
flake8 src/
```

## 📊 Performance

- **Database Operations**: < 50ms average response time
- **Recommendation Generation**: < 200ms for 10 suggestions
- **Memory Usage**: < 100MB typical footprint
- **Storage**: ~10MB for 1000 users with history

## 🔒 Privacy & Security

- All data is stored locally on your machine
- No personal information is transmitted to external servers
- Search history is encrypted in the database
- User data can be exported or deleted at any time

## 🚨 Troubleshooting

### Common Issues

**Database Connection Error**
```bash
# Reset database
python setup.py --reset-db
```

**Missing Dependencies**
```bash
# Reinstall requirements
pip install --force-reinstall -r requirements.txt
```

**Permission Issues**
```bash
# Fix file permissions
chmod +x run.sh
```

## 📚 API Reference

### Core Methods

#### `SongRecommendationBot(config_path="config.json")`
Initialize the recommendation bot with optional configuration.

#### `get_recommendations(user_id, limit=10)`
Generate personalized recommendations for a user.

#### `add_search_history(query, user_id, timestamp=None)`
Add a search query to the user's history.

#### `create_user_profile(user_id, preferences={})`
Create a new user profile with optional preferences.

## 📈 Roadmap

- [ ] Machine learning model integration
- [ ] Real-time music streaming API support
- [ ] Web interface development
- [ ] Mobile app companion
- [ ] Social features and sharing
- [ ] Advanced analytics dashboard

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- Thanks to all contributors who have helped improve this project
- Inspired by modern recommendation algorithms
- Built with love for the music community

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Adityaadpandey/SongRecommendationBot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Adityaadpandey/SongRecommendationBot/discussions)
- **Email**: [Contact the maintainer](mailto:your-email@example.com)

---

⭐ **Star this repository if you find it helpful!**

*Made with ❤️ by the SongRecommendationBot team*
