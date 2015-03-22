class GameSerializer < ActiveModel::Serializer
  attributes(:id,
             :in_progress,
             :team_1_score,
             :team_2_score,
             :team_1,
             :team_2)

  def team_1
    {
      defense: Player.find(object.team_1_defense_id),
      offense: Player.find(object.team_1_offense_id)
    }
  end

  def team_2
    {
      defense: Player.find(object.team_2_defense_id),
      offense: Player.find(object.team_2_offense_id)
    }
  end
end
