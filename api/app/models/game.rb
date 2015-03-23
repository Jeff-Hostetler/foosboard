class Game < ActiveRecord::Base
  belongs_to :team_1_defense, class_name: "Player"
  belongs_to :team_1_offense, class_name: "Player"
  belongs_to :team_2_offense, class_name: "Player"
  belongs_to :team_2_defense, class_name: "Player"

  def self.in_progress?
    where(in_progress: true).count > 0
  end

  def self.goals_scored_for_player(player)
    on_offense(player).reduce(0) do |memo, game|
      if team_1_offense?(game, player)
        memo += game.team_1_score
      else
        memo += game.team_2_score
      end
    end
  end

  def self.goals_against_for_player(player)
    on_defense(player).reduce(0) do |memo, game|
      if team_1_defense?(game, player)
        memo += game.team_2_score
      else
        memo += game.team_1_score
      end
    end
  end

  def self.win_percentage_for_player(player)
    total_games = games_played(player).count
    win_count = games_won(player).count

    if total_games.zero?
      0
    else
      win_count * 100 / total_games
    end
  end

  private

  def self.team_1_offense?(game, player)
    game.team_1_offense_id == player.id
  end

  def self.team_1_defense?(game, player)
    game.team_1_defense_id == player.id
  end

  def self.on_offense(player)
    where("team_1_offense_id = :player_id OR
           team_2_offense_id = :player_id",
           player_id: player.id)
  end

  def self.on_defense(player)
    where("team_1_defense_id = :player_id OR
           team_2_defense_id = :player_id",
           player_id: player.id)
  end

  def self.games_played(player)
    where("team_1_defense_id = :player_id OR
           team_1_offense_id = :player_id OR
           team_2_defense_id = :player_id OR
           team_2_offense_id = :player_id",
           player_id: player.id)
  end

  def self.games_won(player)
    where("((team_1_defense_id = :player_id OR
             team_1_offense_id = :player_id) AND team_1_score = 5)
           OR
           ((team_2_defense_id = :player_id OR
           team_2_offense_id  = :player_id) AND team_2_score = 5)",
           player_id: player.id)
  end
end
