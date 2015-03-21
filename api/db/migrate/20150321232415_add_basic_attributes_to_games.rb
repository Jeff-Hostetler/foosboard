class AddBasicAttributesToGames < ActiveRecord::Migration
  def change
    add_column :games, :team_1_score, :integer, default: 0
    add_column :games, :team_2_score, :integer, default: 0
    add_column :games, :in_progress, :boolean, default: false
  end
end
