class GameSerializer < ActiveModel::Serializer
  attributes(:id,
             :in_progress,
             :team_1_score,
             :team_2_score,
             :team_1,
             :team_2)

  def team_1
    {
      defense: PlayerSerializer.new(object.team_1_defense),
      offense: PlayerSerializer.new(object.team_1_offense)
    }
  end

  def team_2
    {
      defense: PlayerSerializer.new(object.team_2_defense),
      offense: PlayerSerializer.new(object.team_2_offense)
    }
  end
end
