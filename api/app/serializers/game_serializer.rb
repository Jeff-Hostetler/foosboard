class GameSerializer < ActiveModel::Serializer
  attributes(:id,
             :in_progress,
             :team_1_score,
             :team_2_score,
             :team_1,
             :team_2)

  def team_1
    {
      defense: object.team_1_defense,
      offense: object.team_1_offense
    }
  end

  def team_2
    {
      defense: object.team_2_defense,
      offense: object.team_2_offense
    }
  end
end
