class PlayerSerializer < ActiveModel::Serializer
  self.root = false

  attributes(:id,
             :nickname)
end
