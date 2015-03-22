class AddPlayersToGames < ActiveRecord::Migration
  def change
    add_column :games, :team_1_defense_id, :integer, null: false
    add_column :games, :team_1_offense_id, :integer, null: false

    add_column :games, :team_2_offense_id, :integer, null: false
    add_column :games, :team_2_defense_id, :integer, null: false
  end
end
